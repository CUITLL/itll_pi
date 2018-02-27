from datetime import datetime
import os
from pixy import *
from ctypes import *

pixy_init()

REFRESHRATE = 0.1 # Refresh rate in seconds

class Blocks (Structure):
    _fields_ = [ ("type", c_uint),
                 ("signature", c_uint),
                 ("x", c_uint),
                 ("y", c_uint),
                 ("width", c_uint),
                 ("height", c_uint),
                 ("angle", c_uint) ]

blocks = BlockArray(100)

filename = 'data.txt'
filepath = os.path.abspath('/home/mech2018/Shared/'+filename)
open(filepath,'w') # clear data file

i=0
packet=[i,datetime.now(),0,0,0] # i is a placeholder for the coordinates

while(1):
    count = pixy_get_blocks(100,blocks)
    timestamp = datetime.now()
    
    if ((abs(timestamp-packet[1]).total_seconds() > REFRESHRATE) and (count > 0)):
        for index in range (0,count):
            packet = [i,timestamp,blocks[index].signature,blocks[index].x,blocks[index].y] # construct packet [timestamp,i]
            # print(packet[0])
            with open(filepath,'a') as f: # write packet to file, elements tab-seperated (\t), entries line-seperated (\n)
                for item in packet:
                    f.write('%s\t' % item)
                f.write('\n')
            i=i+1
