import os
import subprocess
import click

dropbox = '/Users/benhubsch/Dropbox/'
docs = '/Users/benhubsch/Documents/'
downloads = '/Users/benhubsch/Downloads/'
desktop = '/Users/benhubsch/Dropbox/'
general = '/Users/benhubsch/'

# prompt strings if options not given?
@click.command()
@click.option('-o', '--open-editor', 'result', flag_value='open-editor', help='Opens the file or directory in a text editor.')
@click.option('-c', '--change-directory', 'result', flag_value='change-directory', help='Changes the current working directory. A smarter version of cd <PATH>')
@click.option('-f', '--open-finder', 'result', flag_value='open-finder', help='Opens a new Finder window to the specified directory. If a filename is given, the parent directory of that file is opened.')
@click.option('-d', '--duplicated', is_flag=True, help='To be used when the filename or directory name on your machine is non-unique.')
@click.argument('dst', type=click.Path(), nargs=-1, required=True) # nargs=-1 means that all arguments will be passed as a tuple, no matter how many arguments there are
def cli(dst, result, duplicated):
    print(result)
    print(duplicated)
    # if name.find('.') >= 0:
    #     path = getFilePath(dst, src)
    # else:
    #     path = getFilePath(dst, src)
    # return path


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

