import utils
import fake_gen
import docx_gen
import re
import shutil
import sys

def create_empty_image(filename, size):
    utils.run(f'dd if=/dev/zero of={filename} bs=1M count={size}')

def format_ext4(filename, label='disk'):
    utils.run(f'mkfs.ext4 -E root_owner=$(id -u):$(id -g) -F {filename} -L {label}')

def populate_ext4(filename, name):
    try:
        loop = re.search('/dev/\w*', utils.run(f'udisksctl loop-setup --file {filename}', True)).group()
        mount = re.search('/run/media/([^/]+/[^/]+)$', utils.run(f'udisksctl mount -b {loop}', True)).group() + '/'
        # shutil.copytree(dummy_folder, mount, dirs_exist_ok=True)
        fake_gen.populate_files(mount)
        docx_gen.generate_random_doc(mount + name + '.docx')
        utils.run(f'udisksctl unmount -b {loop}')
        utils.run(f'udisksctl loop-delete -b {loop}')
    except Exception as e:
        print(e, file=sys.stderr)

if __name__ == '__main__':
    filename = 'image.dd'
    create_empty_image(filename, 10)
    format_ext4(filename, 'LucaDomene')
    populate_ext4(filename)
