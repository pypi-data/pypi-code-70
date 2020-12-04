# Residual Dense Network for Image Super-Resolution
# https://arxiv.org/abs/1802.08797

from model import common

import torch
import torch.nn as nn


def make_model(args, parent=False):
    return RDN3D(args)

class RDB_Conv(nn.Module):
    def __init__(self, inChannels, growRate, kSize=3):
        super(RDB_Conv, self).__init__()
        Cin = inChannels
        G = growRate
        self.conv = nn.Sequential(*[
            nn.Conv3d(Cin, G, (3,3,1), padding=(1,1,0), stride=1),
            nn.ReLU()
        ])

    def forward(self, x):
        out = self.conv(x)
        return torch.cat((x, out), 1)


class RDB(nn.Module):
    def __init__(self, growRate0, growRate, nConvLayers, kSize=3):
        super(RDB, self).__init__()
        G0 = growRate0
        G = growRate
        C = nConvLayers

        convs = []
        for c in range(C):
            convs.append(RDB_Conv(G0 + c * G, G))
        self.convs = nn.Sequential(*convs)

        # Local Feature Fusion
        self.LFF = nn.Conv3d(G0 + C * G, G0, 1, padding=0, stride=1)

    def forward(self, x):
        return self.LFF(self.convs(x)) + x


class RDN3D(nn.Module):
    def __init__(self, args):
        super(RDN3D, self).__init__()
        r = args.scale[0]
        G0 = 64
        kSize = args.RDNkSize

        # number of RDB blocks D, conv layers within the blocks C, out channels G within the last layer of the blocks,
        self.D, C, G = {
            'A': (20, 6, 32),
            'B': (16, 8, 64),
            'C': (4, 6, 12),
            'D': (5,4,12)
        }[args.RDNconfig]

        # Shallow feature extraction net
        self.SFENet1 = nn.Conv3d(2, G0, (3,3,1), padding=(1,1,0), stride=1)
        self.SFENet2 = nn.Conv3d(G0, G0, (3,3,1), padding=(1,1,0), stride=1)

        # Redidual dense blocks and dense feature fusion
        self.RDBs = nn.ModuleList()
        for i in range(self.D):
            self.RDBs.append(
                RDB(growRate0=G0, growRate=G, nConvLayers=C)
            )

        # Global Feature Fusion
        self.GFF = nn.Sequential(*[
            nn.Conv3d(self.D * G0, G0, 1, padding=0, stride=1),
            nn.Conv3d(G0, G0, (3,3,1), padding=(1,1,0), stride=1)
        ])

        # Up-sampling net
        self.UPNet = nn.Sequential(*[
            nn.Conv3d(G0, 1, (3,3,1), padding=(1,1,0), stride=1)
        ])

    def forward(self, x):
        f__1 = self.SFENet1(x)
        var = self.SFENet2(f__1)

        RDBs_out = []
        for i in range(self.D):
            var = self.RDBs[i](var)
            RDBs_out.append(var)

        var = self.GFF(torch.cat(RDBs_out, 1))
        var += f__1
        # print(x.shape)
        return self.UPNet(var)+x.mean(1).view(x.size(0), -1, x.size(2),x.size(3),x.size(4))
