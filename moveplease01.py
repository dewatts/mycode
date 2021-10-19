#!/usr/bin/env python3
"""" title """

import shutil
import os

def main():
    """ this is main """

    # change dir
    os.chdir('/home/student/mycode/')

    # move file
    shutil.move('raynor.obj', 'ceph_storage/')

    # prompt
    xname = input('What is the new name for kerrigan.obj? ')

    # rename
    shutil.move('ceph_storage/kerrigan.obj', 'ceph_storage/' + xname)
