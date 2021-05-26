import register
import time

reg = register.Register
tools = register.Utils
watch = register.Monitoring


if __name__ == '__main__':

    process_list = 'PROCESSES'
    check_process_file = watch.Check_External_Process_List(process_list)
    if(check_process_file == -1):
        process_list = watch.PROCESSES
    else:
        process_list = watch.Get_Processes_From_Process_List(process_list)

    print(process_list)
#
    # x = reg.Create_Process_Register(process, 'test')
    # y = reg.Read_Process_Register(process)
#
    # try:
    # assert y[0] == 1, 'Error ocurred'
    # except AssertionError:
    # print('Errors ocurred')
    # else:
    # print('It works')
    # print('Performing registry cleanup...')
    # reg.Clean_Process_Registers(process)
