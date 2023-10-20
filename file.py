#!/usr/bin/python3
from fabric.api import local
def remove_local(number):
    """ method doc
        sudo fab -f 1-pack_web_static.py do_pack
    """
    print(number)
    local("ls -dt versions/* | tail -n +{} ".format(number))
def getNum(number):
    if int(number) == 0:
            number = 1
    number = int(number) + 1
    remove_local(number)
