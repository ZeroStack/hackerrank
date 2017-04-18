#!/bin/python3

import sys


time = input().strip()

def convert_militarytime(time):
    temp_hour = int(time[0:2]) 
    
    am_boolean = time[-2:] == 'AM'
    
    if(am_boolean):
        if(temp_hour == 12):
            temp_hour = temp_hour - 12
            
    else:
        if(temp_hour != 12):
            temp_hour = temp_hour + 12
        
       
    temp_time = str(temp_hour).zfill(2) + time[2:-2]    
        
    print(temp_time)
            
    
convert_militarytime(time)

