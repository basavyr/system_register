import register
import time

reg = register.Register
tools = register.Utils
watch = register.Monitoring


def Execute_Process_Monitor(execution_time, process_list):
    return 1, 1


if __name__ == '__main__':

    process_list_file_name = 'PROCESSES'

    # total execution time of the monitoring process
    execution_time = 10

    watch.Create_External_Process_List(process_list_file_name)
    process_list = watch.Get_Processes_From_Process_List(
        process_list_file_name)

    Execute_Process_Monitor(execution_time, process_list)

    # wipe out the process file at the end of the program execution
    # optional command
    purge_proc_list = False
    if(purge_proc_list == True):
        watch.Purge_External_Process_List(process_list_file_name)
