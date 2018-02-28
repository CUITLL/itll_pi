This repository contains scripts and examples used for the 2018 Mechatronics (MCEN 5115) "Crazy Taxi" project. This file will refer to the Raspberry Pi which is tracking the robots as the "GPS Pi". The following files are of interest:

1.) The 'pixystream/' directory contains the compiled Pixy base code allong with the 'GPS.py' script, which is responsible for pulling beacon coordinates from the Pixy and writing them to a file in '/home/mech2018/Shared'

2.) The 'SCP.py' script is an example for copying the data file from the GPS Pi to a robot's filesystem.

3.) The 'pixyParams_moOffice.prm' file is a configuration file trained to search for pairs of neon sticky notes, configured in Mo's office. Its containing folder is intended as a directory for similar parameter files.

Further instructions are located at the headers of each .py script
