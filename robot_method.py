# -*- coding: utf-8 -*-
"""
Created on Sun Jul 17 21:12:47 2022

@author: stefa
"""
import os
from pyhamilton import (HamiltonInterface,  LayoutManager, 
 Plate96, Tip96, initialize, tip_pick_up, tip_eject, 
 aspirate, dispense,  oemerr, resource_list_with_prefix, normal_logging,
 odtc_connect, odtc_reset, odtc_initialize)

liq_class = 'StandardVolumeFilter_Water_DispenseJet_Empty'



lmgr = LayoutManager('deck.lay')




if __name__ == '__main__': 
    with HamiltonInterface(simulate=True) as ham_int:
        normal_logging(ham_int, os.getcwd())
        initialize(ham_int)
        odtc_id = odtc_connect(ham_int, "192.168.1.2", "192.168.1.50", "", True)
        odtc_reset(ham_int, odtc_id, "", True, 120, "", "")
        odtc_initialize(ham_int, odtc_id, "")