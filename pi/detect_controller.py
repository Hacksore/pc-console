#!/usr/bin/env python
import socket
import time
from wakeonlan import send_magic_packet
import subprocess
from subprocess import Popen, PIPE, CalledProcessError

target_controller_address = 'xdxdxd'
target_pc_address = '04:92:ff:ff:ff:ff'
target_pc_online = False


def check_remote_host():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect((target_pc_address, 445))
        target_pc_online = True
    except socket.error as e:
        target_pc_online = False
    s.close()


# wait for the controller to come online and send WOL packet
with Popen('ubertooth-rx', stdout=PIPE, bufsize=1, universal_newlines=True) as p:
    for line in p.stdout:
        if target_controller_address in line and not target_pc_online:
            send_magic_packet(target_pc_address)
            target_pc_online = True
            print('sending WOL packet')

if p.returncode != 0:
    raise CalledProcessError(p.returncode, p.args)

# check if the remote pc is online via smb port
# query every 250ms
while True:
    check_remote_host()
    time.sleep(0.25)
