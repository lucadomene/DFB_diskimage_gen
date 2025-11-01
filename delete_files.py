import utils
import re
import random

def delete_file(filename, file, hard=False):
    if hard:
        utils.run(f'debugfs -w -R "clri {file}" {filename}')
    utils.run(f'debugfs -w -R "kill_file {file}" {filename}')
    utils.run(f'debugfs -w -R "rm {file}" {filename}')

def get_all_files(filename):
    filenames = []
    docs = utils.run(f'debugfs -R "ls -l Documents" {filename}', capture=True)
    docs_files = docs.splitlines()[2:]
    for line in docs_files:
        parts = line.split()
        filenames.append('Documents/' + parts[-1])

    pics = utils.run(f'debugfs -R "ls -l Pictures" {filename}', capture=True)
    pics_files = pics.splitlines()[2:]
    for line in pics_files:
        parts = line.split()
        filenames.append('Pictures/' + parts[-1])

    return filenames

def random_delete(filename, num=14):
    del_files = random.sample(get_all_files(filename), num)
    hard_del = random.sample(del_files, num//2)
    soft_del = [x for x in del_files if x not in hard_del]
    
    for i in hard_del:
        delete_file(filename, i, hard=True)

    for i in soft_del:
        delete_file(filename, i, hard=False)

if __name__ == '__main__':
    get_all_files('LucaDomene.dd')
