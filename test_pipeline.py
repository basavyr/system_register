#!/usr/bin/env python
from src import pipeline
from src import register
import os
import time


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


if __name__ == '__main__':
    #step1 -> check creation of the process list
    print('Running process file test...')
    Test_Process_File()
