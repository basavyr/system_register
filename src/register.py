import os


class Monitoring:
    """Define all the processes that will be monitored.
    """

    @staticmethod
    def Create_Process_Filename(process_list):
        process_list_file = f'{process_list}.list'
        return process_list_file

    DEFAULT_PROCESSES = {
        "PY": 'python',
        "MD": 'systemd',
        "BASH": 'bash',
        "SH": 'shell'
    }

    @staticmethod
    def Check_External_Process_List(process_list):
        """Check if there is an external file with processes to be monitored"""
        process_list_file = Monitoring.Create_Process_Filename(process_list)
        # checks if theere is an external file with processes
        file_exists = os.path.isfile(process_list_file)

        if(file_exists == False):
            return -1
        else:
            # check if the content of the process list is empty or not
            try:
                with open(process_list_file, 'r+') as reader:
                    procs = reader.readlines()
            except Exception:
                return 1
            if(len(procs) == 0):
                return -1
            return 1

    @staticmethod
    def Get_Processes_From_Process_List(process_list):
        """read the process list (if it exists) and saves them to a list"""
        process_list_file = f'{process_list}.list'
        with open(process_list_file, 'r+') as reader:
            proc_list = reader.readlines()
        proc_list = [x.strip() for x in proc_list]
        return proc_list

    @staticmethod
    def Purge_External_Process_List(process_list):
        process_list_file = Monitoring.Create_Process_Filename(process_list)
        # print(process_list_file)
        file_exists = os.path.isfile(process_list_file)
        # print(file_exists)
        if(file_exists):
            print('Removing external process list file')
            try:
                os.remove(process_list_file)
            except OSError as error:
                print(
                    f'Error while trying to remove the process file\n{error}')
                pass

    @staticmethod
    def Create_External_Process_List(process_list):
        process_list_file = Monitoring.Create_Process_Filename(process_list)
        file_exists = os.path.isfile(process_list_file)

        if(file_exists == False):
            with open(process_list_file, 'w+') as proc_writer:
                for proc in Monitoring.DEFAULT_PROCESSES:
                    proc_writer.write(
                        f'{Monitoring.DEFAULT_PROCESSES[proc]}\n')


class Utils:
    @staticmethod
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
    def Clean_Process_Registers(process):
        process_file = Utils.Register_File(process)
        if os.path.exists(process_file):
            os.remove(process_file)
        else:
            pass

    @staticmethod
    def Purge_Register_Directory(dir_name):
        try:
            dir_path = os.path.realpath(dir_name)
            os.rmdir(dir_path)
        except OSError as err:
            pass
