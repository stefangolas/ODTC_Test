# -*- coding: utf-8 -*-
"""
Created on Sun Jul 17 21:12:47 2022

@author: stefa
"""
import os
from pyhamilton import (HamiltonInterface,  LayoutManager, 
 Plate96, Tip96, initialize, tip_pick_up, tip_eject, 
 aspirate, dispense,  oemerr, resource_list_with_prefix, normal_logging,
 odtc_connect, odtc_reset, odtc_initialize, odtc_get_status, odtc_download_protocol,
 odtc_open_door, odtc_close_door, odtc_execute_protocol, odtc_terminate, odtc_read_actual_temperature,
 ph_initialize, ph_wakeup, ph_measure)

import sys
import time

liq_class = 'StandardVolumeFilter_Water_DispenseJet_Empty'



lmgr = LayoutManager('deck.lay')



if __name__ == '__main__': 
    with HamiltonInterface(simulate=True) as ham_int:
        normal_logging(ham_int, os.getcwd())
        initialize(ham_int)
        
        odtc_id = odtc_connect(ham_int, local_ip = "192.168.1.2", device_ip = "192.168.1.50", simulation_mode = True)
        odtc_reset(ham_int, odtc_id, simulation_mode = True, timeout = 120)
        odtc_initialize(ham_int, odtc_id)
        status = odtc_get_status(ham_int, odtc_id) # Doesn't return anything in simulation mode
        
        odtc_download_protocol(ham_int, odtc_id, protocol_file = 'abc.xml')
        
        odtc_open_door(ham_int, odtc_id)
        odtc_close_door(ham_int, odtc_id)
        
        odtc_execute_protocol(ham_int, odtc_id, 'protocol', 1)
        
        protocol_time = 15
        protocol_finish_time = time.time() + protocol_time
        while time.time() < protocol_finish_time:
            odtc_read_actual_temperature(ham_int, odtc_id)
            time.sleep(5)
        
        odtc_close_door(ham_int, odtc_id)
        odtc_terminate(ham_int, odtc_id)
        
        
        