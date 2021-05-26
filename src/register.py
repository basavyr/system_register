import os


class Utils:
    def Create_Output_File(process):
        file_name = f'{process}_instances.list'


class Register:

    @staticmethod
    def Create_Register_Directory(dir_name):
        try:
            os.mkdir(dir_name)
        except OSError:
            pass

    @staticmethod
    def Read_Process_Register(process):
        process_file_name = Utils.Create_Output_File(process)

        # read content from file
        try:
            with open(process_file_name, 'r+') as reader:
                instances = reader.readlines()
        except FileNotFoundError:
            instances = ' '

        if(instances == ' '):
            return -1
        return f'{len(instances)} -> {instances}'


if __name__ == '__main__':
    print('Register class works')
