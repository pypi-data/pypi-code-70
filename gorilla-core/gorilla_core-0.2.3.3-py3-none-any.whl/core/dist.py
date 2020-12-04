# Copyright (c) Open-MMLab. All rights reserved.
import os
import functools
import subprocess

import torch
import torch.distributed as dist
import torch.multiprocessing as mp

# # NOTE: avoid RuntimeError: received 0 items of ancdata
# mp.set_sharing_strategy("file_system")


def init_dist(launcher, backend="nccl", **kwargs):
    if mp.get_start_method(allow_none=True) is None:
        mp.set_start_method("spawn")
    if launcher == "pytorch":
        _init_dist_pytorch(backend, **kwargs)
    elif launcher == "slurm":
        _init_dist_slurm(backend, **kwargs)
    else:
        raise ValueError("Invalid launcher type: {}".format(launcher))


def _init_dist_pytorch(backend, **kwargs):
    rank = int(os.environ["RANK"])
    world_size = int(os.environ["WORLD_SIZE"])
    num_gpus = torch.cuda.device_count()
    torch.cuda.set_device(rank % num_gpus)
    kwargs.update(backend=backend, rank=rank, world_size=world_size)
    print("dist_parameters: ", kwargs)
    dist.init_process_group(**kwargs)


def _init_dist_slurm(backend, port=None):
    r"""Initialize slurm distributed training environment.

    If argument ``port`` is not specified, then the master port will be system
    environment variable ``MASTER_PORT``. If ``MASTER_PORT`` is not in system
    environment variable, then a default port ``29500`` will be used.

    Args:
        backend (str): Backend of torch.distributed.
        port (int, optional): Master port. Defaults to None.
    """
    proc_id = int(os.environ["SLURM_PROCID"])
    ntasks = int(os.environ["SLURM_NTASKS"])
    node_list = os.environ["SLURM_NODELIST"]
    num_gpus = torch.cuda.device_count()
    torch.cuda.set_device(proc_id % num_gpus)
    addr = subprocess.getoutput(
        "scontrol show hostname {} | head -n1".format(node_list))
    # specify master port
    if port is not None:
        os.environ["MASTER_PORT"] = str(port)
    elif "MASTER_PORT" in os.environ:
        pass  # use MASTER_PORT in the environment variable
    else:
        # 29500 is torch.distributed default port
        os.environ["MASTER_PORT"] = "29500"
    os.environ["MASTER_ADDR"] = addr
    os.environ["WORLD_SIZE"] = str(ntasks)
    os.environ["RANK"] = str(proc_id)
    dist.init_process_group(backend=backend)


def get_dist_info():
    if dist.is_available():
        initialized = dist.is_initialized()
    else:
        initialized = False
    if initialized:
        rank = dist.get_rank()
        world_size = dist.get_world_size()
    else:
        rank = 0
        world_size = 1
    return rank, world_size


def master_only(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        rank, _ = get_dist_info()
        if rank == 0:
            return func(*args, **kwargs)

    return wrapper
