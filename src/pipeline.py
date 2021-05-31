from . import register
from . import process_monitor as procmon
import time


def now():
    return time.time()


reg = register.Register
tools = register.Utils
watch = register.Monitoring


def Execute_Process_Monitor(execution_time, process_list):

    debug_mode = False

    runtime = True

    idx = 1

    current_instance_stack = []
    previous_instance_stack = []

    start_time = now()
    while(runtime):

        print(f'\nIteration #{idx}...\n')

        for process in process_list:
            # if(debug_mode):
            # print(f'<<{process}>>')
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
                current_instance_stack.append(process_active_instances_number)
                if(process_active_instances_number == 0):
                    if(debug_mode):
                        print(
                            f'<<{process}>> -> No active instances found')
                else:
                    if(debug_mode):
                        print(
                            f'( {process_active_instances_number} ) Active instances found\n{process_active_instances_list}')
                    if(debug_mode):
                        print(
                            f'<<{process}>> -> {process_active_instances_number} active instances found')
        if(idx > 1 and len(current_instance_stack) and len(previous_instance_stack)):
            changes = procmon.Process.Check_Instance_Change(
                current_instance_stack, previous_instance_stack)
            print(
                f'Active instances for all processes: <<{current_instance_stack}>>')
            procmon.Process.Check_Process_Stop(process_list,
                                               current_instance_stack, previous_instance_stack)

        # stop the execution pipeline after the runtime reachers execution time
        if(now() - start_time >= execution_time):
            runtime = False
            break

        # continue the monitor loop if the total runtime does not exceed the allowed execution
        idx += 1
        previous_instance_stack = list(current_instance_stack)
        current_instance_stack.clear()
        time.sleep(1)

    if(runtime == False and idx > 1):
        return 1
    return 0


def Create_Process_List():
    # Create the process list and save it to a file
    watch.Create_External_Process_List(
        register.Register.process_list_file_name)
    PROCESS_LIST = watch.Get_Processes_From_Process_List(
        register.Register.process_list_file_name)
    return PROCESS_LIST


def SayHi():
    return 'hi'


if __name__ == '__main__':

    PIPELINE = True

    PIPELINE_CLEANUP = True

    PIPELINE_EXECUTION_TIME = 30

    if(PIPELINE == True):
        # PROCESS_LIST = Create_Process_List()
        PROCESS_LIST = ['python']
        PIPELINE_EXECUTION = Execute_Process_Monitor(
            PIPELINE_EXECUTION_TIME, PROCESS_LIST)
        if(PIPELINE_EXECUTION == 1 and PIPELINE_CLEANUP == True):
            print('Doing cleanup...')
            reg.Clean_All(reg.register_directory)
            watch.Purge_External_Process_List(reg.process_list_file_name)
        elif(PIPELINE_EXECUTION == 0):
            print('The process monitor failed...')
