from datetime import datetime
import os

REFRESHRATE = 0.1 # Refresh rate in seconds

filename = 'data.txt'
filepath = os.path.abspath('/home/mech2018/Shared/'+filename)
open(filepath,'w') # clear data file

i=0
packet=[datetime.now(),i] # i is a placeholder for the coordinates

while(1):
    timestamp = datetime.now()
    if abs(timestamp-packet[0]).total_seconds() > REFRESHRATE:
        packet = [timestamp,i] # construct packet [timestamp,i]
        # print(packet[0])
        with open(filepath,'a') as f: # write packet to file, elements tab-seperated (\t), entries line-seperated (\n)
            for item in packet:
                f.write('%s\t' % item)
            f.write('\n')
        i=i+1
