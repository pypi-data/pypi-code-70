#!/usr/bin/env python
# -*- coding: ascii -*-

r"""
RocketIsp calculates delivered Isp for liquid rocket thrust chambers.

RocketIsp uses a simplified JANNAF approach to calculate delivered
specific impulse (Isp) for liquid rocket thrust chambers.

RocketIsp
Copyright (C) 2020  Applied Python

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""
import io
import os
here = os.path.abspath(os.path.dirname(__file__))

__author__ = 'Charlie Taylor'
__copyright__ = 'Copyright (c) 2020 Charlie Taylor'
__license__ = 'GPL-3'
#exec( open(os.path.join( here,'_version.py' )).read() )  # creates local __version__ variable
from rocketisp._version import __version__
__email__ = "cet@appliedpython.com"
__status__ = "4 - Beta" # "3 - Alpha", "4 - Beta", "5 - Production/Stable"

from math import pi
from scipy import optimize
import numpy as np

from rocketprops.rocket_prop import get_prop
from rocketprops.unit_conv_data import get_value # for any units conversions
from rocketisp.efficiency.eff_pulsing import eff_pulse
from rocketisp.efficiency.eff_divergence import eff_div
from rocketisp.efficiency.effBL_NASA_SP8120 import eff_bl_NASA, regen_corrected_bl

from rocketisp.efficiency.calc_full_pcentLossBL import calc_pcentLossBL
from rocketisp.efficiency.calc_noz_kinetics import calc_IspODK

#from rocketisp.nozzle.cd_throat import get_Cd
from rocketisp.nozzle.calc_full_Cd import calc_Cd
from rocketisp.stream_tubes import CoreStream
from rocketisp.efficiencies import Efficiencies
from rocketisp.goldSearch import search_max, search_min
from rocketisp.mr_range import MRrange

AVAIL_EFF_MODEL_D   = {} # index=eff name, value=list of recognized model names
AVAIL_EFF_MODEL_D['Pulse'] = ['rough estimate']
AVAIL_EFF_MODEL_D['Div'] = ['simple fit', 'MLP fit']
AVAIL_EFF_MODEL_D['BL'] = ['MLP fit', 'NASA-SP8120']
AVAIL_EFF_MODEL_D['Kin'] = ['MLP fit']
AVAIL_EFF_MODEL_D['Em'] = ['Rupe']
AVAIL_EFF_MODEL_D['Mix'] = ['mixAngle']
AVAIL_EFF_MODEL_D['Vap'] = ['Lgen']


selected_eff_modelD = {}# index=eff name, value= name of selected efficiency model
selected_eff_modelD['Pulse'] = 'rough estimate'
selected_eff_modelD['Div'] = 'simple fit'
selected_eff_modelD['BL'] = 'MLP fit'
selected_eff_modelD['Kin'] = 'MLP fit'
selected_eff_modelD['Em'] = 'Rupe'
selected_eff_modelD['Mix'] = 'mixAngle'
selected_eff_modelD['Vap'] = 'Lgen'

class RocketThruster(object):
    """
    RocketIsp calculates delivered Isp for liquid rocket thrust chambers by
    simplified JANNAF method.
    
    :param name: name of RocketThruster
    :param coreObj: CoreStream object
    :param injObj: Injector object (optional)
    :param noz_regen_eps: regen cooled nozzle area ratio
    :param pulse_sec: s,duration of pulsing engine (default = infinity)
    :param pulse_quality: on a scale of 0.0 to 1.0, how good is engine at pulsing
    :param isRegenCham: flag to indicate chamber is regen cooled
    :param calc_CdThroat: flag to trigger calc_CdThroat
    :type name: str
    :type coreObj: CoreStream
    :type injObj: Injector
    :type noz_regen_eps: float
    :type pulse_sec: float
    :type pulse_quality: float
    :type isRegenCham: bool
    :type calc_CdThroat: bool
    :return: RocketThruster object
    :rtype: RocketThruster
    """
    
    def set_eff_model(self, eff_name='Div', model_name='MLP fit'):
        """
        Change the named efficiency model from the default model to a different model.
        For example, change from the simple nozzle divergence model (Div) to the 
        Multi-Layer Perceptron (MLP) divergence model.

        :param eff_name: name of efficiency (e.g. Div, BL, Kin)
        :param model_name: name of model to be used (must be in AVAIL_EFF_MODEL_D)
        :type eff_name: str
        :type model_name: str
        :return: None
        :rtype: None        
        """
        if eff_name in AVAIL_EFF_MODEL_D:
            if model_name in AVAIL_EFF_MODEL_D[ eff_name ]:
                selected_eff_modelD[ eff_name ] = model_name
            else:
                raise Exception('in set_eff_model, "%s" is not a recognized model name for %s.'%(model_name, eff_name) )
                
        else:
            raise Exception('in set_eff_model, "%s" is not a recognized efficiency name'%eff_name)
        
        
    def __call__(self, name):
        return getattr(self, name ) # let it raise exception if no name attr.

    def __init__(self, name='RocketIsp Thruster',
                 coreObj=CoreStream(), injObj=None, noz_regen_eps=1.0, 
                 pulse_sec=float('inf'), pulse_quality=0.8,
                 isRegenCham=False, calc_CdThroat=True):
        """
        Calculate delivered thrust chamber Isp by simplified JANNAF method.
        """
        self.name          = name
        self.coreObj       = coreObj
        self.geomObj       = coreObj.geomObj
        self.injObj        = injObj
        
        #self.iprop         = coreObj.oxName + '/' + coreObj.fuelName
        self.pulse_sec     = pulse_sec
        self.pulse_quality = pulse_quality  
        
        self.noz_regen_eps = noz_regen_eps
        self.isRegenCham    = isRegenCham   

        self.calc_CdThroat  = calc_CdThroat
        
                
        self.calc_all_eff()
    
    @property
    def iprop(self):
        return self.coreObj.oxName + '/' + self.coreObj.fuelName
    
    def reset_attr(self, name, value, re_evaluate=True):
        """
        reset the value of any existing attribute of RocketThruster instance.
        If re_evaluate is True, then call self.evaluate() after resetting the value of the attribute.
        """
        if hasattr( self, name ):
            setattr( self, name, value )
        else:
            raise Exception('Attempting to set un-authorized RocketThruster attribute named "%s"'%name )
            
        if re_evaluate:
            self.calc_all_eff()
    
    def set_eps_to_equal_pexit(self, Pexit_psia=14.7):
        """
        Iterate on Area Ratio to find desired Pexit
        """
        ceaObj = self.coreObj.ceaObj
        MR = self.coreObj.MRcore
        eps = self.coreObj.geomObj.eps
        
        eps_min = 2.0
        eps_max = 200.0
        
        def get_diff_sq( eps ):
        
            Pexit = self.coreObj.Pc / ceaObj.get_PcOvPe( Pc=self.coreObj.Pc, MR=MR, eps=eps)
            return (Pexit - Pexit_psia)**2

            
        eps_opt, diff_min  = search_min(get_diff_sq, eps_min, eps_max, tol=1.0E-9)
        self.coreObj.geomObj.reset_attr('eps', eps_opt, re_evaluate=True)
        self.calc_all_eff()
        
        return eps_opt
    
    def set_mr_to_max_ispdel(self):
        """
        Iterate on MRcore to find the peak Isp
        """
        # get MR for equivalence ratio = 1
        MRstart = self.coreObj.ceaObj.getMRforER( ERr=1.0 )
        
        MRlo = MRstart / 3.0
        MRhi = MRstart * 3.0
        
        def get_ispdel( MR ):
            self.coreObj.reset_attr('MRcore', MR, re_evaluate=True)
            self.calc_all_eff()
            return self.coreObj.IspDel
            
        MRcore_opt, IspMax  = search_max(get_ispdel, MRlo, MRhi, tol=0.01)
        #print('MRcore_opt=%g, IspMax=%g sec'%(MRcore_opt, IspMax) )
        # use MRcore_opt to reset everything
        self.coreObj.reset_attr('MRcore', MRcore_opt, re_evaluate=True)
        self.calc_all_eff()
        
        return MRcore_opt

    
    def scale_Rt_to_Thrust(self, ThrustLbf=500.0, Pamb=0.0, use_scipy=False):
        """
        Adjust throat size in order to get total thrust at specified ambient pressure exactly

        :param ThrustLbf: lbf, desired thrust at specified ambient pressure (Pamb)
        :param Pamb: psia, ambient pressure
        :param use_scipy: flag to indicate the need for more sophisticated root finder
        :type ThrustLbf: float
        :type Pamb: float
        :type use_scipy: bool
        :return: None
        :rtype: None        """
        
        Pamb_save = Pamb
        self.coreObj.reset_attr( 'Pamb', Pamb, re_evaluate=True)
        
        def f_diff( Rt ):
            self.geomObj.reset_attr( 'Rthrt', Rt, re_evaluate=True)
            #self.coreObj.evaluate()
            self.calc_all_eff()
            return ThrustLbf - self.coreObj.Fambient
        
        At_guess = self.geomObj.At * ThrustLbf / self.coreObj.Fambient
        Rt_guess = (At_guess/pi)**0.5
        
        if use_scipy:
            # demand convergence to a tolerance with a root solver.
            Rt_min = Rt_guess/1.4
            Rt_max = Rt_guess*1.4
            
            sol = optimize.root_scalar(f_diff, x0=Rt_guess, bracket=[Rt_min, Rt_max], 
                                       xtol=ThrustLbf/1.0E8, method='brentq')
            #print('sol.root=%g, sol.iterations=%g, sol.function_calls=%g'%(sol.root, sol.iterations, sol.function_calls))
            f_diff( sol.root )
        else:
            # often converges in just a few iterations.
            xtol=ThrustLbf/1.0E8
            
            #print( 'self.coreObj.Fambient',self.coreObj.Fambient )
            f_diff( Rt_guess )
            #print( 'self.coreObj.Fambient',self.coreObj.Fambient )
            for _ in range( 10 ):
                At_guess = self.geomObj.At * ThrustLbf / self.coreObj.Fambient
                Rt_guess = (At_guess/pi)**0.5
                err = f_diff( Rt_guess )
                #print( 'self.coreObj.Fambient',self.coreObj.Fambient )
                if abs(err) < xtol:
                    self.coreObj.reset_attr( 'Pamb', Pamb_save, re_evaluate=True)
                    return
        self.coreObj.reset_attr( 'Pamb', Pamb_save, re_evaluate=True)
        
    
    def calc_all_eff(self):
        """
        Looks at the efficiency object (effObj) and calculates those efficiencies
        that have not been set as constants by the user.
        
        see: self.calc_CdThroat or effObj['XXX'].is_const for individual efficiencies
        """
        DOREVAL = False
        made_a_change = False
        effObj = self.coreObj.effObj
        
        if self.calc_CdThroat:
            #CdThroat = get_Cd( RWTU=self.geomObj.RupThroat, gamma=self.coreObj.gammaChm )
            CdThroat = calc_Cd( Pc=self.coreObj.Pc, Rthrt=self.geomObj.Rthrt, RWTU=self.geomObj.RupThroat )
            
            self.coreObj.reset_CdThroat( CdThroat, method_name='MLP fit', re_evaluate=DOREVAL)
            made_a_change = True
                    
        #if self.calc_effPulse:
        if not effObj['Pulse'].is_const:
            effPulse = eff_pulse( pulse_sec=self.pulse_sec, pulse_quality=self.pulse_quality)
            msg = 'rough estimate (%g sec, Q=%g)'%(self.pulse_sec, self.pulse_quality)
            self.coreObj.effObj.set_value( 'Pulse', effPulse, value_src=msg, re_evaluate=DOREVAL)
            made_a_change = True
        
        #if self.calc_effDiv:
        if not effObj['Div'].is_const:
            
            # AVAIL_EFF_MODEL_D['Div'] = ['simple fit', 'MLP fit']
            if selected_eff_modelD['Div'] == 'simple fit':            
                effDiv = eff_div( eps=self.geomObj.eps, pcBell=self.geomObj.pcentBell)
                msg = selected_eff_modelD['Div'] + ' eps=%g, %%bell=%g'%(self.geomObj.eps, self.geomObj.pcentBell)
                
            elif selected_eff_modelD['Div'] == 'MLP fit':            
                raise Exception('MLP fit not yet implemented for eff Div')
            
                
            self.coreObj.effObj.set_value( 'Div', effDiv, value_src=msg, re_evaluate=DOREVAL)
            made_a_change = True
        
        #if self.calc_effBL:
        if not effObj['BL'].is_const:
            
            # AVAIL_EFF_MODEL_D['BL'] = ['MLP fit', 'NASA-SP8120']
            if selected_eff_modelD['BL'] == 'NASA-SP8120':
                effBL = eff_bl_NASA( Dt=self.geomObj.Rthrt*2.0, Pc=self.coreObj.Pc, eps=self.geomObj.eps)
            elif selected_eff_modelD['BL'] == 'MLP fit':
                
                pclossBL = calc_pcentLossBL( Pc=self.coreObj.Pc, eps=self.geomObj.eps, 
                                             Rthrt=self.geomObj.Rthrt, pcentBell=self.geomObj.pcentBell, 
                                             TcCham=self.coreObj.TcODE )
                                            
                effBL = (100.0 - pclossBL)/100.0
            
            msg = selected_eff_modelD['BL']
            
            if self.noz_regen_eps > 1.0:
                msg += 'regen-corrected'
                effBL = regen_corrected_bl( eff_bl=effBL, eps=self.geomObj.eps, noz_regen_eps=self.noz_regen_eps )
                
            self.coreObj.effObj.set_value( 'BL', effBL, value_src=msg, re_evaluate=DOREVAL)
            made_a_change = True
        
        #if self.calc_effKin:
        if not effObj['Kin'].is_const:
            IspODK = calc_IspODK(self.coreObj.ceaObj, Pc=self.coreObj.Pc, eps=self.geomObj.eps, 
                                 Rthrt=self.geomObj.Rthrt, pcentBell=self.geomObj.pcentBell, 
                                 MR=self.coreObj.MRcore)
                        
            # coreObj has made IspODE calc already
            effKin = IspODK / self.coreObj.IspODE
            msg = selected_eff_modelD['Kin']
            
            self.coreObj.effObj.set_value( 'Kin', effKin, value_src=msg, re_evaluate=DOREVAL)
            made_a_change = True
        
        if self.injObj is not None:
            #if self.calc_effEm:
            if not effObj['Em'].is_const:
                effEm = self.injObj.calculate_effEm()
                msg = 'Rupe elemEm=%g'%self.injObj.elemEm
                self.coreObj.effObj.set_value( 'Em', effEm, value_src=msg, re_evaluate=DOREVAL)
                made_a_change = True
                
            #if self.calc_effMix:
            if not effObj['Mix'].is_const:
                effMix = self.injObj.calculate_effMix() # calc inter-element mixing efficiency (2 deg estimate)
                msg = 'mixAngle=%.2f deg'%self.injObj.mixAngle
                self.coreObj.effObj.set_value( 'Mix', effMix, value_src=msg, re_evaluate=DOREVAL)
                made_a_change = True
            
            #if self.calc_effVap:
            if not effObj['Vap'].is_const:
                effVap = self.injObj.calculate_effVap()
                msg = 'gen vaporized length'
                self.coreObj.effObj.set_value( 'Vap', effVap, value_src=msg, re_evaluate=DOREVAL)
                made_a_change = True
        
        # after all updates, re_evaluate
        if made_a_change:
            self.coreObj.evaluate()
        
        
    def summ_print(self):
        """
        print to standard output, the current state of RocketThruster instance.
        """
        print( self.get_summ_str() )
        
    def get_summ_str(self):        
        """
        return string of the current state of RocketThruster instance.
        """
        output = io.StringIO()
        def add( *args, **kwargs ):
            print(*args, file=output, **kwargs)
        
        add('='*30, ' %s '%self.name, '='*30)
        
        c = self.coreObj.get_summ_str()
        print(c, file=output)

        if self.injObj is not None:
            c =self.injObj.get_summ_str(show_core_stream=False)
            print(c, file=output)
            
        # collect string output
        contents = output.getvalue()
        output.close()
        return contents        
        
    def plot_isp_curves(self, title='', png_name='', pixel_wh=None,
                      do_show=True, show_grid=True, Npts=30, edge_frac=0.97 ):
        import matplotlib.pyplot as plt
        import pylab
        prop_cycle = pylab.rcParams['axes.prop_cycle']
        colorsL = prop_cycle.by_key()['color']
        
        
        if pixel_wh is None:
            fig, ax = plt.subplots(nrows=1, ncols=1)
        else:
            w,h = pixel_wh
            fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(w/100.0, h/100.0), dpi=100)
        
        mrr = MRrange(self.coreObj.ceaObj, Pc=self.coreObj.Pc, eps=self.geomObj.eps,
                      edge_frac=edge_frac)
        mrlo, mrhi = mrr.get_mr_range()
        
        ispodeL  = [] # list of IspODE  (one-dimensional equilibrium)
        ispodkL  = [] # list of IspODK  (one-dimensional kinetic)
        ispdel_coreL = [] # list of Isp Core delivered
        ispdelL = [] # list of Isp thruster delivered
        ispdel_ambL = [] # list of IspAmb thruster delivered
        ispodfL  = [] # list of IspODF  (frozen)
        
        
        mrcoreL  = np.linspace(mrlo, mrhi, Npts) # array of MRcore  (core stream tube mixture ratio)
        mrthrusterL = []
        
        MRsave = self.coreObj.MRcore
        
        for mr in mrcoreL:
            self.coreObj.reset_attr( 'MRcore', mr, re_evaluate=True)
            self.calc_all_eff()

            ispodeL.append( self.coreObj.IspODE )
            ispodkL.append( self.coreObj.IspODK )
            ispodfL.append( self.coreObj.IspODF )
            
            ispdel_coreL.append( self.coreObj.IspDel_core )
            ispdelL.append( self.coreObj.IspDel )
            ispdel_ambL.append( self.coreObj.IspAmb )
            mrthrusterL.append( self.coreObj.MRthruster )
            
        self.coreObj.reset_attr( 'MRcore', MRsave, re_evaluate=True)
        self.calc_all_eff()
        
        plt.plot( mrcoreL, ispodeL, label='IspODE', color=colorsL[0] )
        plt.plot( mrcoreL, ispodkL, label='IspODK', color=colorsL[1] )
        plt.plot( mrcoreL, ispodfL, label='IspODF', color=colorsL[2] )
        if self.coreObj.barrierObj is not None:
            plt.plot( mrcoreL, ispdel_coreL, ':', label='IspDel_core', color=colorsL[4] )
        plt.plot( mrthrusterL, ispdelL, '--', linewidth=3, label='IspDel vac', color=colorsL[3] )

        if self.coreObj.Pamb > 0.0:
            plt.plot( mrthrusterL, ispdel_ambL, '--', linewidth=1, label='IspAmbient', color=colorsL[5] )
        
        MRdes_pt = self.coreObj.MRthruster
        plt.plot( [MRdes_pt], [self.coreObj.IspDel], 'D', markersize=8, color=colorsL[3] )
        
        ymin, ymax = ax.get_ylim()
        dy = 0.03 * (ymax - ymin)
        ax.text(MRdes_pt, self.coreObj.IspDel+dy, 'Des Pt', color=colorsL[3])
        
        if self.coreObj.Pamb > 0.0:
            isp_max = max(ispdel_ambL)
            i = ispdel_ambL.index( isp_max )
            isp = ispdel_ambL[i]
            ax.text(mrthrusterL[i], isp+dy, 'Pamb=%g psia'%self.coreObj.Pamb, 
                    color=colorsL[5], ha='center')

        if show_grid:
            plt.grid()
        plt.legend(loc='best')
        plt.ylabel( 'Isp (sec)' )
        if self.coreObj.add_barrier:
            plt.xlabel( 'Mixture Ratio (Core and Thruster)' )
        else:
            plt.xlabel( 'Mixture Ratio' )
            
        if not title:
            title = self.iprop + '\nPc=%g psia, AreaRatio=%g:1'%(self.coreObj.Pc, self.geomObj.eps ) +\
                       ', Rt=%g in'%self.geomObj.Rthrt
            if self.coreObj.add_barrier:
                title += ', FFC=%g%%'%self.coreObj.barrierObj.pcentFFC
                
        plt.title( title )
        
        fig.tight_layout()
        
        if png_name:
            if not png_name.endswith('.png'):
                png_name = png_name + '.png'
            plt.savefig( png_name )
        
        if do_show:
            plt.show()
            
        return plt
        
    def plot_eff_curves(self, title='', png_name='', pixel_wh=None,
                      do_show=True, show_grid=True, Npts=30, edge_frac=0.97 ):
        import matplotlib.pyplot as plt
        import pylab
        prop_cycle = pylab.rcParams['axes.prop_cycle']
        colorsL = prop_cycle.by_key()['color']
        
        
        if pixel_wh is None:
            fig, ax = plt.subplots(nrows=1, ncols=1)
        else:
            w,h = pixel_wh
            fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(w/100.0, h/100.0), dpi=100)
        
        mrr = MRrange(self.coreObj.ceaObj, Pc=self.coreObj.Pc, eps=self.geomObj.eps,
                      edge_frac=edge_frac)
        mrlo, mrhi = mrr.get_mr_range()
        
        mrcoreL  = np.linspace(mrlo, mrhi, Npts) # array of MRcore  (core stream tube mixture ratio)
        mrthrusterL = []
        
        MRsave = self.coreObj.MRcore
        
        eff_ispL = []
        eff_ereL = []
        eff_nozL = []
        
        eff_kinL = [] # 'Div','Kin','BL'
        eff_divL = []
        eff_blL  = []
        
        eff_mixL = [] # 'Mix','Em','Vap'
        eff_emL  = []
        eff_vapL = []
        
        effObj = self.coreObj.effObj
        
        for mr in mrcoreL:
            self.coreObj.reset_attr( 'MRcore', mr, re_evaluate=True)
            self.calc_all_eff()
            
            if not effObj.effD['Isp'].is_const:
                eff_nozL.append( effObj['Noz'].value )
                eff_ereL.append( effObj['ERE'].value )
                
            if not effObj.effD['Noz'].is_const:
                eff_kinL.append( effObj['Kin'].value )
                eff_divL.append( effObj['Div'].value )
                eff_blL.append(  effObj['BL'].value )
                
            if not effObj.effD['ERE'].is_const:
                eff_mixL.append( effObj['Mix'].value )
                eff_emL.append(  effObj['Em'].value )
                eff_vapL.append( effObj['Vap'].value )
            
            eff_ispL.append( effObj.effD['Isp'].value )
            mrthrusterL.append( self.coreObj.MRthruster )
            
        self.coreObj.reset_attr( 'MRcore', MRsave, re_evaluate=True)
        self.calc_all_eff()
        
        if eff_ereL:
            plt.plot( mrcoreL, eff_ereL, linewidth=3, label='effERE', color=colorsL[0] )
        if eff_nozL:
            plt.plot( mrcoreL, eff_nozL, linewidth=3, label='effNoz', color=colorsL[1] )
                
                
        plt.plot( mrcoreL, eff_ispL, '-', linewidth=3, label='effIsp', color=colorsL[3] )
        
        MRdes_pt = self.coreObj.MRcore
        plt.plot( [MRdes_pt], [effObj.effD['Isp'].value], 'D', markersize=8, color=colorsL[3] )
        
        ymin, ymax = ax.get_ylim()
        dy = 0.03 * (ymax - ymin)
        ax.text(MRdes_pt, effObj.effD['Isp'].value+dy, 'Des Pt', color=colorsL[3])
        
        ax.set_ylim( (ymin-dy, 1.0) )


        ncol = 1
        if eff_nozL:
            if eff_kinL:
                ncol += 1
                dataL = sorted( [(eff_kinL[0], eff_kinL, 'effKin','--'), 
                                 (eff_divL[0], eff_divL, 'effDiv',':'), 
                                 (eff_blL[0], eff_blL, 'effBL','-.')], reverse=True )
                for (_, effL, label, sline) in dataL:
                    plt.plot( mrcoreL, effL, sline, label=label,  color=colorsL[1] )
                
        if eff_ereL:
            if min(eff_ereL) < 0.991 and eff_mixL:
                ncol += 1
                dataL = sorted( [(eff_mixL[0], eff_mixL, 'effMix','--'), 
                                 (eff_emL[0], eff_emL, 'effEm',':'), 
                                 (eff_vapL[0], eff_vapL, 'effVap','-.')], reverse=True )
                for (_, effL, label, sline) in dataL:
                    plt.plot( mrcoreL, effL, sline, label=label,  color=colorsL[0] )
                
                
                #plt.plot( mrcoreL, eff_mixL, '--', label='effMix',  color=colorsL[0] )
                #plt.plot( mrcoreL,  eff_emL, ':', label='effEm',  color=colorsL[0] )
                #plt.plot( mrcoreL, eff_vapL, '-.', label='effVap',  color=colorsL[0] )
        
        if show_grid:
            plt.grid()
        plt.legend(loc='best', ncol=ncol)
        
        
        plt.ylabel( 'Efficiency' )
        if self.coreObj.add_barrier:
            plt.xlabel( 'Mixture Ratio (Core and Thruster)' )
        else:
            plt.xlabel( 'Mixture Ratio' )
            
        if not title:
            title = self.iprop + '\nPc=%g psia, AreaRatio=%g:1'%(self.coreObj.Pc, self.geomObj.eps ) +\
                       ', Rt=%g in'%self.geomObj.Rthrt
            if self.coreObj.add_barrier:
                title += ', FFC=%g%%'%self.coreObj.barrierObj.pcentFFC
                
        plt.title( title )
        
        fig.tight_layout()
        
        if png_name:
            if not png_name.endswith('.png'):
                png_name = png_name + '.png'
            plt.savefig( png_name )
        
        if do_show:
            plt.show()
            
        return plt

if __name__ == '__main__':
    from rocketisp.geometry import Geometry
    
    from rocketisp.injector import Injector
    from rocketisp.efficiencies import Efficiencies
    
    geomObj = Geometry(Rthrt=5.868/2,
                       CR=2.5, eps=150,  pcentBell=80, 
                       RupThroat=1.5, RdwnThroat=1.0, RchmConv=1.0, cham_conv_deg=30,
                       LchmOvrDt=3.10, LchmMin=2.0, LchamberInp=16)
    
    effObj = Efficiencies()
    #effObj.set_const('ERE', 0.98)
    
    core = CoreStream( geomObj, effObj, oxName='N2O4', fuelName='MMH',  MRcore=1.85,
                 Pc=150, CdThroat=0.995,
                 pcentFFC=14.0, ko=0.035)
    
    inj = Injector(core, Tox=None, Tfuel=None, elemEm=0.9,
                   fdPinjOx=0.25, fdPinjFuel=0.25,
                   elemDensInp=None, NelementsInp=None,
                   setNelementsBy='acoustics', # can be "acoustics", "density", "input"
                   setAcousticFreqBy='mode', # can be "mode" or "freq"
                   #desAcousMode=0.8*4.2012, desFreqInp=2000,
                   desAcousMode='1T',
                   OxOrfPerEl=1.0, FuelOrfPerEl=1.0, 
                   lolFuelElem=True, 
                   CdOxOrf=0.75, CdFuelOrf=0.75, dropCorrOx=1, dropCorrFuel=1,
                   DorfMin=0.008,
                   LfanOvDorfOx=20.0, LfanOvDorfFuel=20.0)
    
    C = RocketThruster(name='Sample Thruster',coreObj=core, injObj=inj, pulse_sec=float('inf'), pulse_quality=0.8)
                 
    #C.scale_Rt_to_Thrust( 10000.0, Pamb=0.0, use_scipy=False )
    C.summ_print()
    
    #print( C.iprop )
    C.set_mr_to_max_ispdel()
    C.plot_isp_curves( title='', png_name='', pixel_wh=None,
                      do_show=False, show_grid=True, Npts=30, edge_frac=0.97 )
    C.plot_eff_curves( title='', png_name='', pixel_wh=None,
                      do_show=True, show_grid=True, Npts=30, edge_frac=0.97 )
                      
                      
    
