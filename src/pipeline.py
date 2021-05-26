import register
import time

reg = register.Register
tools = register.Utils
watch = register.Monitoring


if __name__ == '__main__':

    process = watch.PROCESSES["PY"]

    x = reg.Create_Process_Register(process, 'test')
    y = reg.Read_Process_Register(process)

    try:
        assert y[0] == 1, 'Error ocurred'
    except AssertionError:
        print('Errors ocurred')
    else:
        print('It works')
        time.sleep(2)
        print('Performing registry cleanup...')
        reg.Clean_Process_Registers(process)
