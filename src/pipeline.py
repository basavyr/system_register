import register
import time

reg = register.Register
tools = register.Utils
watch = register.Monitoring


if __name__ == '__main__':

    process_list_file_name = 'PROCESSES'

    watch.Create_External_Process_List(process_list_file_name)
    process_list = watch.Get_Processes_From_Process_List(
        process_list_file_name)
    print(process_list)
    # watch.Purge_External_Process_List(process_list_file_name)
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
