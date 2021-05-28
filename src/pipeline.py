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
                print(f'will analyze active instances for <<{process}>>')
            grepped_ps_command = procmon.Utils.make_ps_grep_process(process)
            procmon.Process.Run_Shell_Command(grepped_ps_command)
            process_active_instances_number, process_active_instances_list = procmon.Process.Get_Active_Instances(
                process)
            try:
                assert process_active_instances_number >= 0, f'Issue while counting the active instances for [{process}]'
            except AssertionError:
                print(
                    f'Issue while counting the active instances for [{process}]')
            else:
                if(process_active_instances_number == 0):
                    print(
                        f'No active instances found')
                else:
                    print(
                        f'( {process_active_instances_number} ) Active instances found\n{process_active_instances_list}')

        # stop the execution pipeline after the runtime reachers execution time
        if(now() - start_time >= execution_time):
            runtime = False
            break
        idx += 1
        time.sleep(5)

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

    CLEANUP = True

    EXECUTION_TIME = 3

    if(PIPELINE == True):
        PIPELINE_EXECUTION = Execute_Process_Monitor(
            EXECUTION_TIME, PROCESS_LIST)
        if(PIPELINE_EXECUTION and CLEANUP == True):
            print('Doing cleanup...')
            reg.Clean_All(reg.register_directory)
            watch.Purge_External_Process_List(reg.process_list_file_name)
