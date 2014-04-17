#coding: UTF-8

import platform
import os

def get_platform_name():
    '''Returns current platform the seafile server is running on. Possible return
    values are:

    - 'linux'
    - 'windows'
    - 'raspberry-pi'

    '''
    if os.name == 'nt':
        return 'windows'
    elif 'arm' in platform.machine():
        return 'raspberry-pi'
    else:
        return 'linux'


def compare_seafile_server_version(va, vb):
    '''Compare two version strings va and vb:
    1.2.3 > 1.2.2
    1.2.3 < 1.2.10

    va == vb -> return 0
    va > vb -> return 1
    va < vb -> return -1
    '''
    try:
        la = [ int(x) for x in va.split('.') ]
        lb = [ int(x) for x in vb.split('.') ]
    except:
        return 0

    return cmp(la, lb)