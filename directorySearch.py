import os
import subprocess
import sys
import click

dropbox = '/Users/benhubsch/Dropbox/'
docs = '/Users/benhubsch/Documents/'
downloads = '/Users/benhubsch/Downloads/'
desktop = '/Users/benhubsch/Dropbox/'
general = '/Users/benhubsch/'


@click.command()
@click.option('-u', '--unique', default=True, help='File name on your machine')
@click.argument('name', required=True)
def cli(name, general):
    if name.find('.') >= 0:
        path = getFilePath(name, general)
    else:
        path = getFilePath(name, general)
    return path


def getFilePath(fname, path):
    for root, dirs, files in os.walk(path):
        if fname in dirs:
            return os.path.join(root, fname)

def getDirPath(dname, path):
    for root, dirs, files in os.walk(path):
        if fname in files:
            console.log(os.path.join(root, fname))
            return os.path.join(root, fname)


# def find_all_files(name, path):
#     result = []
#     for root, dirs, files in os.walk(path):
#         if name in files:
#             result.append(os.path.join(root, name))
#     return result
#
# def find_directory(name, path):
#     for root, dirs, files in os.walk(path):
#         if name in dirs:
#             return os.path.join(root, name)
#
# def formatter(path):
#     return ('\ ').join(path.split(' '))
#
# os.chdir(find_directory('Practice Problems', '/Users/benhubsch'))
# os.system('/bin/bash')

# for file_instance in find_all_files('redditBot.py', '/Users/benhubsch/'):
#     os.system('atom ' + formatter(file_instance))
# os.system('atom ' + formatter(find_first_file('redditBot.py', '/Users/benhubsch/')))

# print(sys.argv)
# print(sys.argv[1])

# os.chdir(dropbox)
# os.system("pwd")
# os.system("/bin/bash")
# subprocess.Popen(['open','/Users/benhubsch/Dropbox/'])

