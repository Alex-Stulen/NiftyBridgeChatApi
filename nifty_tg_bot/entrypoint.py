import os


def run_cmd(command: str):
    return os.system(command)


run_cmd('python run.py')
