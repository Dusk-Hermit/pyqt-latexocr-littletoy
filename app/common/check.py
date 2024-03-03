import platform
import subprocess

def get_os_type():
    return platform.system()

def construct_command(cmd):
    os_type=get_os_type()
    if os_type=='Windows':
        return f'where {cmd}'
    elif os_type=='Linux':
        return f'which {cmd}'
    else:
        raise Exception('Unsupported OS type')

def execute_cmd(cmd):
    result=subprocess.run(cmd,shell=True,capture_output=True,text=True)
    return result.returncode ==0

def cmd_exists(cmd):
    return execute_cmd(construct_command(cmd))

if __name__ == "__main__":
    if cmd_exists('latex'):
        print('latex is installed')
    else:
        print('latex is not installed')