import register
import time
import process_monitor as procmon


def now():
    return time.time()


reg = register.Register
tools = register.Utils
watch = register.Monitoring


def Execute_Process_Monitor(execution_time, process_list):

    runtime = True

    idx = 1

    start_time = now()
    while(runtime):

        # TODO do operations

        print(f'Iteration {idx}...\n')

        for process in process_list:
            print(f'will analyze instances for {process}')
            procmon.Process.RunCommand(process)

        if(now()-start_time >= execution_time):
            runtime = False
            break
        idx += 1
        time.sleep(1)


if __name__ == '__main__':

    process_list_file_name = 'PROCESSES'
    watch.Create_External_Process_List(process_list_file_name)
    process_list = watch.Get_Processes_From_Process_List(
        process_list_file_name)

    # total execution time of the monitoring process
    execution_time = 3
    Execute_Process_Monitor(execution_time, process_list)

    # wipe out the process file at the end of the program execution (optional command)
    purge_proc_list = True
    if(purge_proc_list == True):
        watch.Purge_External_Process_List(process_list_file_name)
