#!/usr/bin/env python
import os
import subprocess
import time
import register


class Utils:
    """Helper class that creates output files, deals with string encoding/decoding and much more"""

    utf8 = 'UTF-8'

    @staticmethod
    def encode(obj): return bytes(obj, Utils.utf8)

    @staticmethod
    def decode(text): return text.decode(Utils.utf8)

    @staticmethod
    def create_file(file_name): return f'{file_name}_command_output.dat'

    @staticmethod
    def get_process_file(
        process_name): return f'{process_name}_command_output.dat'

    @staticmethod
    def make_ps_grep_process(process): return f'ps aux | grep {process}'

    @staticmethod
    def Return_Error_Tuple():
        """
        Return a safe-mode tuple [output,error] when the command that was executed by Popen could not finish successfully
        """
        return '-1', 'Command could not be executed'

    @staticmethod
    def Bash_Execution(command):
        shell_cmd = ['/bin/bash', '-c', str(command)]
        return shell_cmd

    @staticmethod
    def Save_Output(command_name, command_output):
        filename = Utils.create_file(command_name)

        # if the output object is in bytes, convert it to string
        if(Utils.Is_Bytes(command_output) == 1):
            command_output = Utils.decode(command_output)

        # create a directory where every process will have the running instances saved as files
        register.Register.Create_Register_Directory(
            register.Register.register_directory)

        # adjust the path of the output file for each process according to the directory used for storage
        file_path = f'{register.Register.register_directory}/{filename}'

        with open(file_path, 'w+') as writer:
            try:
                writer.write(command_output)
            except TypeError:
                command_output = Utils.decode(command_output)
                writer.write(command_output)

    @staticmethod
    def extract_process_name(full_command):
        stripped = full_command.split(' ')
        return stripped[-1]

    @staticmethod
    def Is_Bytes(input):
        try:
            assert type(input) == bytes, 'The input object is not bytes'
        except AssertionError:
            return -1
        return 1


class Process:

    @staticmethod
    def Check_Process_Completion(command):
        try:
            assert command.returncode == 0, 'Unexpected error ocurred'
        except AssertionError as err:
            print(f'There was an issue:\n{err}')
            return -1
        else:
            print(f'The command {command} has finished properly')
            return 1

    @staticmethod
    def Get_Command_Status(command):
        try:
            assert command.returncode == 0, 'Unexpected error ocurred'
        except AssertionError:
            return 'NOT OK'
        else:
            return 'OK'

    @staticmethod
    def Check_Active_Instances(command_output_file):
        with open(command_output_file, 'r+') as reader:
            active_instances = reader.readlines()
        return active_instances

    @staticmethod
    def Get_Active_Instances(process):
        """
        Searches for every instances which belongs to `process` that is running on the machine with a given PID.
        Returns a tuple, with the total number of instances and a list of all instances. 

        """
        process_file = Utils.get_process_file(process)
        # the path of the process file must be changed to the directory in which the lists are stored
        register_process_file = f'{register.Register.register_directory}/{process_file}'
        try:
            with open(register_process_file, 'r+') as reader:
                instances = reader.readlines()
        except FileNotFoundError:
            instances = []
        n_instances = len(instances)
        # the real number of active instances is N-2
        # one instance is from the grep itself, the other is for the python script
        real_instances = n_instances - 2
        if(real_instances == 0):
            return 0, []
        if(real_instances < 0):
            return -1, []
        return real_instances, instances

    @staticmethod
    def Check_Instance_Change(current_stack, previous_stack):
        changes = [current_stack[idx] - previous_stack[idx]
                   for idx in range(len(current_stack))]
        return(changes)

    @staticmethod
    def Instance_Internal_State(instance_change):
        return 1

    @staticmethod
    def Check_Process_Stop(process_list, current_stack, previous_stack):
        """shows which processes have instances that stopped running"""
        instance_changes = Process.Check_Instance_Change(
            current_stack, previous_stack)

        idx = 0
        for proc in zip(process_list, instance_changes):
            proc_name = proc[0]
            proc_instances_change = proc[1]
            if(proc_instances_change == 0):
                print(f'<<{proc_name}>> | No changes within instances')
            elif proc_instances_change < 0:
                print(
                    f'<<{proc_name}>> | {abs(proc_instances_change)} stopped instances')
            elif proc_instances_change > 0:
                print(
                    f'<<{proc_name}>> | {abs(proc_instances_change)} new spawned instances')

    @staticmethod
    def Run_Shell_Command(command):
        """
        Execute a shell-specific command within a Python method

        Uses the Popen function, from the subprocess module

        """
        debug_mode = False

        # run a command with the shell-mode turned off
        # the shell=False mode requires the prefix of the command to be the system's shell executable
        # the usual shell for UNIX-based systems is /usr/bin/bash
        non_shell_mode = True

        bash_command = Utils.Bash_Execution(command)
        if(debug_mode):
            print(f'shell command: {bash_command}')

        command_name = Utils.extract_process_name(command)
        if(debug_mode):
            print(f'command name: {command_name}')

        # execute the command outside the interactive shell
        if(non_shell_mode):
            # the command is called within a safe-mode try/except block
            try:
                executed_command_noShell = subprocess.Popen(bash_command,
                                                            stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            except FileNotFoundError as error:
                if(debug_mode):
                    print('There was an issue during command execution')
                output, errors = Utils.Return_Error_Tuple()
                if(debug_mode):
                    print(f'Error: {error}')
                if(debug_mode):
                    print(
                        f'Command output/errors:\nSTDOUT: {output}\nSTDERR: {errors}')
            except OSError as error:
                if(debug_mode):
                    print('There was an [OS] issue during command execution')
                output, errors = Utils.Return_Error_Tuple()
                if(debug_mode):
                    print(
                        f'Command output/errors:\nSTDOUT: {output}\nSTDERR: {errors}')
                if(debug_mode):
                    print(f'[OS] Error: {error}')
            else:
                # If no errors occur during the command execution
                try:
                    output, errors = executed_command_noShell.communicate(
                        timeout=10)
                    if(debug_mode):
                        print(f'Command <<{command}>> was executed')
                except subprocess.TimeoutExpired:
                    executed_command_noShell.kill()
                    output, errors = Utils.Return_Error_Tuple()
                    if(debug_mode):
                        print('The executed command has reached the timeout limit')
                        print(
                            f'Command output/errors:\nSTDOUT: {output}\nSTDERR: {errors}')
                except OSError as os_issue:
                    executed_command_noShell.kill()
                    output, errors = Utils.Return_Error_Tuple()
                    if(debug_mode):
                        print(f'There was an [OS] issue.\n{os_issue}\n')
                        print(f'Command runtime error: {errors}')
                else:
                    if(debug_mode):
                        print(
                            f'Return code: {executed_command_noShell.returncode} ({Process.Get_Command_Status(executed_command_noShell)})')
                    if(Utils.Is_Bytes(output)):
                        Utils.Save_Output(command_name, output)
