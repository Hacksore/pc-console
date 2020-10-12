#!/usr/bin/env python
import socket
import sys
import time
import os
from wakeonlan import send_magic_packet
from subprocess import Popen, PIPE, CalledProcessError
import threading
from dotenv import load_dotenv

load_dotenv()

TARGET_CONTROLLER_ADDRESS = os.getenv("TARGET_CONTROLLER_ADDRESS")
TARGET_PC_MAC_ADDRESS = os.getenv("TARGET_PC_MAC_ADDRESS")
TARGET_PC_IP_ADDRESS = os.getenv("TARGET_PC_IP_ADDRESS")

# start with the assumption it's online
target_pc_online = True

def check_for_controller():
    global target_pc_online

    print('controller data check started')
    with Popen('ubertooth-rx', stdout=PIPE, bufsize=1, universal_newlines=True) as p:
        for line in p.stdout:
            if TARGET_CONTROLLER_ADDRESS in line and not target_pc_online:
                send_magic_packet(TARGET_PC_MAC_ADDRESS)
                target_pc_online = True
                print('sending WOL packet to ' + TARGET_PC_MAC_ADDRESS)

    if p.returncode != 0:
        raise CalledProcessError(p.returncode, p.args)


def check_remote_host():
    print('remote host health check started')
    global target_pc_online

    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(1)
            s.connect((TARGET_PC_IP_ADDRESS, 3389))
            s.close()
            target_pc_online = True
        except socket.error:
            target_pc_online = False
        time.sleep(0.50)


if __name__ == '__main__':

    try:
        # start bin watcher
        p1 = threading.Thread(target=check_for_controller)
        p1.start()

        # # start pc helth checker
        p2 = threading.Thread(target=check_remote_host)
        p2.start()

    except KeyboardInterrupt:
        sys.exit()
