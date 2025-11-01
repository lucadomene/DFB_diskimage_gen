import create_ext4
import delete_files
import utils
import argparse

def generate_forensic_image(name):
    filename = name + '.dd'
    create_ext4.create_empty_image(filename, 10)
    create_ext4.format_ext4(filename, name)
    create_ext4.populate_ext4(filename, name)
    delete_files.random_delete(filename)
    delete_files.delete_file(filename, name + '.docx')

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', '--student-name')
    utils.check_tools(['mkfs.ext4', 'dd', 'mount', 'umount', 'fls', 'debugfs'])
    args = parser.parse_args()
    generate_forensic_image(args.student_name)
