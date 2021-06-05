#!/usr/bin/env python


import os
import time
import sys


try:
    sys.path.insert(1, '../')
    import src.process_monitor as procmon
    import src.pipeline as pipeline
except ModuleNotFoundError:
    sys.path.insert(1, '')
    import src.pipeline as pipeline
    import src.process_monitor as procmon
else:
    print('Importing finished ✅')


register = procmon.Register
monitor = procmon.Monitoring


def Test_Process_File():
    pipeline.Create_Process_List()

    process_list_file = monitor.Create_Process_Filename(
        register.process_list_file_name)

    proc_file = os.path.isfile(process_list_file)

    fail_status = 1

    if(proc_file):
        # print('Success')
        os.remove(process_list_file)
        fail_status = 0

    if(fail_status):
        print('Test failed! ❌')
    else:
        print('Success! ✅')


def Test_Cleaning_Procedure():
    fail_value = 1
    try:
        # adjust the pipeline such that the register directory is above the tests
        new_dir = '../src/' + register.register_directory
        # print(os.path.abspath (new_dir))
        # print(os.path.isdir(new_dir))
        register.Clean_All(new_dir)
    except Exception:
        fail_value = 1
        # print(f'in total cleaning -> {exc}')
    else:
        fail_value = 0

    if(fail_value == 0):
        print('Success! ✅')
    else:
        print('Test failed! ❌')


if __name__ == '__main__':
    # step1 -> check creation of the process list
    print('Running process file test...')
    Test_Process_File()
    print('Running process file cleaning...')
    Test_Cleaning_Procedure()
