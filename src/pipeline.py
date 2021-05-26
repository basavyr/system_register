import register


reg = register.Register


if __name__ == '__main__':

    x = reg.Create_Process_Register('bash', 'test')
    y = reg.Read_Process_Register('bash')

    try:
        assert y[0] == 1, 'Error ocurred'
    except AssertionError:
        print('Errors ocurred')
    else:
        print('It works')
