#!/usr/bin/env python
from src import pipeline
from src import register
import os


x = pipeline.Create_Process_List()

# register.Monitoring.Purge_External_Process_List(
#     register.Register.process_list_file_name)
print(x)
