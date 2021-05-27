import register
import time
import process_monitor as procmon


def now():
    return time.time()


reg = register.Register
tools = register.Utils
watch = register.Monitoring


def Execute_Process_Monitor(execution_time, process_list):

    debug_mode = True

    runtime = True

    idx = 1

    start_time = now()
    while(runtime):

        print(f'\nIteration #{idx}...\n')

        for process in process_list:
            if(debug_mode):
                print(f'will analyze instances for {process}')
            grepped_ps_command = procmon.Utils.make_ps_grep_process(process)
            procmon.Process.Run_Shell_Command(grepped_ps_command)

        # stop the execution pipeline after the runtime reachers execution time
        if(now() - start_time >= execution_time):
            runtime = False
            break
        idx += 1
        time.sleep(1)

    if(runtime == False and idx):
        return 1
    return 0


if __name__ == '__main__':

    PIPELINE = True

    # Create the process list and save it to a file
    watch.Create_External_Process_List(
        register.Register.process_list_file_name)
    PROCESS_LIST = watch.Get_Processes_From_Process_List(
        register.Register.process_list_file_name)

    EXECUTION_TIME = 10

    if(PIPELINE == True):
        PIPELINE_EXECUTION = Execute_Process_Monitor(
            EXECUTION_TIME, PROCESS_LIST)
        if(PIPELINE_EXECUTION):
            reg.Clean_All(reg.register_directory)
