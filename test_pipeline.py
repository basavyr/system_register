#!/usr/bin/env python
from src import pipeline
from src import register
import os
import time


def Test_Process_File():
    processes = pipeline.Create_Process_List()

    process_list_file = register.Monitoring.Create_Process_Filename(
        register.Register.process_list_file_name)

    proc_file = os.path.isfile(process_list_file)

    if(proc_file):
        # print('Success')
        os.remove(process_list_file)
        return 1

    return -1


if __name__ == '__main__':
    print('Running process file test...')
    x = Test_Process_File()
    if(x == 1):
        print('Success!')
    else:
        print('Test failed.')
