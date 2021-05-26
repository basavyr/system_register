import os


class Utils:
    def Register_File(process):
        file_name = f'{process}_instances.list'
        return file_name


class Register:

    @staticmethod
    def Create_Register_Directory(dir_name):
        try:
            os.mkdir(dir_name)
        except OSError:
            pass

    @staticmethod
    def Read_Process_Register(process):
        process_file_name = Utils.Register_File(process)

        # read content from file
        try:
            with open(process_file_name, 'r+') as reader:
                instances = reader.readlines()
        except FileNotFoundError:
            instances = ' '

        if(instances == ' '):
            return -1, instances
        return 1, instances

    @staticmethod
    def Create_Process_Register(process, process_output):
        process_file_name = Utils.Register_File(process)

        # writes the output to a file
        # only write to file if no error occurs
        try:
            with open(process_file_name, 'w+') as writer:
                writer.write(process_output)
        except OSError:
            return -1
        return 1

    @staticmethod
    def Clean_Process_Registers(process_file):
        if os.path.exists(process_file):
            os.remove(process_file)
        else:
            pass


if __name__ == '__main__':
    print('Register class works')
