# Before running this script, it is important to install the following:
### 1.) Install cryptography: 
###     $ sudo apt-get install build-eddential libssl-dev libffi-dev python3-dev
###     $ sudo pip install cryptography --no-binary cryptography
### 2.) Install paramiko:
###     $ sudo pip install paramiko
### 3.) Install scp:
###     $ sudo pip install scp

import paramiko
from scp import SCPClient

def createSSHClient(server, port, user, password):
    client = paramiko.SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(server, port, user, password)
    return client

# GPS Pi's IP is 172.21.77.166 ... use port 22 ... username is 'mech2018' ... passwd is 'mcen5115'
ssh = createSSHClient('172.21.77.166', 22, 'mech2018', 'mcen5115')
scp = SCPClient(ssh.get_transport())

# Add a second argument to tell scp where to place the copied file
# Data will be published to 'data.txt', located at '/home/mech2018/Shared'
scp.get('/home/mech2018/Shared/data.txt')
