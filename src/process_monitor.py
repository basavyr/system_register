#!/usr/bin/env python
import os
import subprocess
import time


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
    def search_running_process(process): return f'ps aux | grep {process}'

    @staticmethod
    def Return_Error_Tuple():
        """
        Return a safe-mode tuple [output,error] when the command that was executed by Popen could not finish successfully
        """
        return '-1', 'Command could not be executed'

    @staticmethod
    def Make_Shell_Command(command):
        shell_cmd = ['/bin/bash', '-c', str(command)]
        return shell_cmd

    @staticmethod
    def Save_Output(command_name, command_output):
        filename = Utils.create_file(command_name)

        # if the output object is in bytes, convert it to string
        if(Utils.Accept_Bytes(command_output) == -1):
            command_output = Utils.decode(command_output)

        with open(filename, 'w+') as writer:
            try:
                writer.write(command_output)
            except TypeError:
                command_output = Utils.decode(command_output)
                writer.write(command_output)

    @staticmethod
    def extract_name(full_command):
        stripped = full_command.split(' ')
        return stripped[-1]

    @staticmethod
    def Accept_Bytes(input):
        try:
            assert type(input) == bytes, 'The input object is not bytes'
        except AssertionError:
            return 1
        return -1


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
        process_file = Utils.create_file(Utils.extract_name(process))
        try:
            with open('dada', 'r+') as reader:
                instances = reader.readlines()
        except FileNotFoundError:
            instances = ' '
        n_instances = len(instances)
        # the real number of active instances is N-2
        # one instance is from the grep itself, the other is for the python script
        real_instances = n_instances-2
        if(real_instances == 0 or instances == ' '):
            return -1
        return real_instances

    @staticmethod
    def RunCommand(command):
        """
        Execute a shell-specific command within a Python method

        Uses the Popen function, from the subprocess module

        """
        debug_mode = True

        # cannot run ps command in non-shell mode
        non_shell_mode = False

        shell_cmd = Utils.Make_Shell_Command(command)
        if(debug_mode):
            print(f'shell command: {shell_cmd}')

        command_name = Utils.extract_name(command)
        if(debug_mode):
            print(f'command name: {command_name}')

        # execute the command outside the interactive shell
        if(non_shell_mode):
            if(debug_mode):
                print('SHELL mode is turned OFF')
            # the command is called within a safe-mode try/except block
            try:
                executed_command_noShell = subprocess.Popen(shell_cmd,
                                                            stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            except FileNotFoundError:
                if(debug_mode):
                    print('There was an issue during command execution')
                output, errors = Utils.Return_Error_Tuple()
                if(debug_mode):
                    print(
                        f'Command output/errors:\nSTDOUT: {output}\nSTDERR: {errors}')
            else:
                # If no errors occur during the command execution
                try:
                    output, errors = executed_command_noShell.communicate(
                        timeout=10)
                    print(f'Command <<{command}>> was executed')
                except subprocess.TimeoutExpired:
                    executed_command_noShell.kill()
                    output, errors = Utils.Return_Error_Tuple()
                    if(debug_mode):
                        print(
                            f'Command output/errors:\nSTDOUT: {output}\nSTDERR: {errors}')
                except OSError as os_issue:
                    if(debug_mode):
                        print(f'There was an OS-specific issue.\n{os_issue}')
                        print(errors)
                except Exception as problem:
                    if(debug_mode):
                        print(
                            f'There was an issue while trying to execute the command:\n{problem}')
                else:
                    if(debug_mode):
                        print(
                            f'Return code: {executed_command_noShell.returncode} ({Process.Get_Command_Status(executed_command_noShell)})')
                    if(Utils.Accept_Bytes(output)):
                        if(debug_mode):
                            print(f'Command output -> Saved into its output file...')
                        Utils.Save_Output(command_name, output)
