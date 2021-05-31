#!/usr/bin/env python


import os
import time
import sys


try:
    from ..src import pipeline
    from ..src import process_monitor
    from ..src import register
except ImportError:
    sys.path.append('../')
    from src import pipeline
    from src import process_monitor
    from src import register


def Test_Process_File():
    pipeline.Create_Process_List()

    process_list_file = register.Monitoring.Create_Process_Filename(
        register.Register.process_list_file_name)

    proc_file = os.path.isfile(process_list_file)

    fail_status = 1

    if(proc_file):
        # print('Success')
        os.remove(process_list_file)
        fail_status = 0

    if(fail_status):
        print('Test failed.')
    else:
        print('Success!')


def Test_Cleaning_Procedure():
    fail_value = 1
    try:
        dirname = register.Register.register_directory
        register.Register.Clean_All(dirname)
        print(dirname)
    except Exception as exc:
        fail_value = 1
        print(exc)
    else:
        fail_value = 0

    if(fail_value == 0):
        print('Success!')
    else:
        print('Test failed.')


if __name__ == '__main__':
    # step1 -> check creation of the process list
    print('Running process file test...')
    Test_Process_File()
    print('Running process file cleaning...')
    Test_Cleaning_Procedure()
