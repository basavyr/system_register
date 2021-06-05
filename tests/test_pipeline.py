#!/usr/bin/env python


import os
import time
import sys


try:
    sys.path.insert(1, '../')
    import src.process_monitor as procmon
    import src.pipeline as pipeline
    import src.register as register
except ModuleNotFoundError:
    sys.path.insert(1, '')
    import src.register as register
    import src.pipeline as pipeline
    import src.process_monitor as procmon
else:
    print('Importing finished ✅')


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
        print('Test failed! ❌')
    else:
        print('Success! ✅')


def Test_Cleaning_Procedure():
    fail_value = 1
    try:
        # adjust the pipeline such that the register directory is above the tests
        new_dir = '../src/' + register.Register.register_directory
        # print(os.path.abspath (new_dir))
        # print(os.path.isdir(new_dir))
        register.Register.Clean_All(new_dir)
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
