import os


class Register:
    @staticmethod
    def Create_Register_Directory(dir_name):
        try:
            os.mkdir(dir_name)
        except OSError:
            pass
