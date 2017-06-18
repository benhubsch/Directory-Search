import os
import subprocess
import click
from errors import PathError
from userinfo import paths

# prompt strings if options not given?
@click.command()
@click.option('-o', '--open-editor', 'result', flag_value='open-editor', help='Opens the file or directory in a text editor.')
@click.option('-c', '--change-directory', 'result', flag_value='change-directory', help='Changes the current working directory. A smarter version of cd <PATH>')
@click.option('-f', '--open-finder', 'result', flag_value='open-finder', help='Opens a new Finder window to the specified directory. If a filename is given, the parent directory of that file is opened.')
@click.option('-d', '--duplicated', is_flag=True, help='To be used when the filename or directory name on your machine is non-unique.')
@click.argument('dst', type=click.Path(), nargs=-1, required=True) # nargs=-1 means that all arguments will be passed as a tuple, no matter how many arguments there are
def cli(dst, result, duplicated):
    dst = (' ').join(dst)
    if duplicated:
        arr = list(getAllPaths(dst))
        if len(arr) > 1:
            click.echo(str(len(arr)) + ' paths found that match your input.\n')
            for dex in range(len(arr)):
                click.echo(str(dex + 1) + ': ' + str(arr[dex]))
            click.echo()
            value = click.prompt('Enter a path number to proceed: ', type=int)
            path = arr[value - 1]
        else:
            path = arr[0]
    else:
        path = getOnePath(dst)
        
    click.echo(path)


def formatter(path):
    final = ''
    for i in range(len(path) - 1):
        if path[i + 1] == ' ' and path[i] != '\\':
            final += path[i] + '\\'
        else:
            final += path[i]
    return final + path[-1]

def getFilePath(fname, path, all=False):
    found = set([])
    for root, dirs, files in os.walk(path):
        if fname in files:
            if all:
                found.add(os.path.join(root, fname))
            else:
                # print(os.path.join(root, fname))
                return os.path.join(root, fname)
    return list(found)

def getDirPath(dname, path):
    found = set([])
    for root, dirs, files in os.walk(path):
        if dname in dirs:
            if all:
                found.add(os.path.join(root, dname))
            else:
                return os.path.join(root, dname)
    return list(found)

def getAllPaths(dst):
    topFound = set([])
    for startDirectory in paths:   # notion of already having visited a directory and not re-searching it
        if dst.find('.') >= 0:
            pathArr = getFilePath(dst, startDirectory, True)
        else:
            pathArr = getDirPath(dst, startDirectory)

        if pathArr != []:
            for path in pathArr:
                topFound.add(formatter(path))

    if topFound == set([]):
        raise PathError('Path to file/directory not found.')
    return topFound

def getOnePath(dst):
    for startDirectory in paths:
        if dst.find('.') >= 0:
            path = getFilePath(dst, startDirectory)
        else:
            path = getDirPath(dst, startDirectory)

        if path != None:
            return formatter(path)

    raise PathError('Path to file/directory not found.')


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

