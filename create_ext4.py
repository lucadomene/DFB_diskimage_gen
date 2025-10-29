import utils

def create_empty_image(filename, size):
    utils.run(f'dd if=/dev/zero of={filename} bs=1M count={size}')

def format_ext4(filename, label='disk'):
    utils.run(f'mkfs.ext4 -F {filename} -L {label}')

if __name__ == '__main__':
    filename = 'image.dd'
    create_empty_image(filename, 10)
    format_ext4(filename, 'LucaDomene')
