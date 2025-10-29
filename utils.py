import subprocess
import shutil
import sys

def run(cmd, capture=False):
    if capture:
        p = subprocess.run(cmd, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return p.stdout.decode().strip()
    else:
        subprocess.run(cmd, check=True, shell=True)

def check_tools(tools):
    for t in tools:
        if shutil.which(t) is None:
            print(f'Error: required tool \'{t}\' not found in PATH', file=sys.stderr)
            sys.exit(1)

if __name__ == '__main__':
    output = run('ls -l', capture=True)
    print(output)

    check_tools(['mkfs.ext4', 'dd', 'mount', 'umount'])
