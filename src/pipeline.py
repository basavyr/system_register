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

        # TODO do operations

        print(f'\nIteration #{idx}...\n')

        for process in process_list:
            if(debug_mode):
                print(f'will analyze instances for {process}')
            procmon.Process.Run_Shell_Command(process)

        if(now() - start_time >= execution_time):
            runtime = False
            break
        idx += 1
        time.sleep(1)


if __name__ == '__main__':

    PIPELINE = True

    # Create the process list and save it to a file
    watch.Create_External_Process_List(
        register.Register.process_list_file_name)
    process_list = watch.Get_Processes_From_Process_List(
        register.Register.process_list_file_name)
    print(process_list)

    EXECUTION_TIME = 10
