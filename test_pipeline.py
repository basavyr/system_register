#!/usr/bin/env python
from src import pipeline
from src import register
import os
import time

processes = pipeline.Create_Process_List()

process_list_file = register.Monitoring.Create_Process_Filename(
    register.Register.process_list_file_name)

proc_file = os.path.isfile(process_list_file)

if(proc_file):
    print('Success')

if(proc_file):
    os.remove(process_list_file)
