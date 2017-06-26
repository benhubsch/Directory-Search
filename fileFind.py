import os
import subprocess
import click
from userinfo import paths, editor
from os.path import expanduser

class PathError(Exception):
    pass

# making it case insensitive, autocomplete possible (remembering old values, running and building a trie when terminal loads)?,
# adding an option to search if path not found on a try/catch

@click.command()
@click.option('-c', '--change-directory', 'result', flag_value='change-directory', help='Changes the current working directory. A smarter version of cd <PATH>.  This flag is the default when no other flag is provided.')
@click.option('-e', '--open-editor', 'result', flag_value='open-editor', help='Opens the file or directory in a text editor.')
@click.option('-f', '--open-finder', 'result', flag_value='open-finder', help='Opens a new Finder window to the specified directory. If a filename is given, the parent directory of that file is opened.')
@click.option('-d', '--duplicated', is_flag=True, help='To be used when the filename or directory name on your machine is non-unique.')
@click.argument('dst', type=click.Path(), nargs=-1, required=True) # nargs=-1 means that all arguments will be passed as a tuple, no matter how many arguments there are
def cli(dst, result, duplicated):
    dst = (' ').join(dst)
    try:
        path = callHandler(dst, duplicated, paths)
    except Exception as e:
        click.echo('The file or directory you requested was not located in any of your default, built-in filepaths.')
        whole = click.prompt('Would you like to search everything in your file tree starting from your home directory? This could take a little while depending on the size of your file tree. (y/n)')
        while whole != 'y' and whole != 'n':
            click.echo('\'y\' or \'n\' are the only valid responses')
            whole = click.prompt('Would you like to search everything in your file tree starting from your home directory? (y/n)')
        try:
            if whole == 'y':
                home = expanduser("~")
                path = callHandler(dst, duplicated, [home])
            else:
                click.secho('File not found.', fg='red', bold=True)
                return
        except Exception as e:
            click.secho('File not found.', fg='red', bold=True)
            return
    dealWithResult(path, result)

def callHandler(dst, duplicated, start):
    if duplicated:
        arr = list(getAllPaths(dst, start))
        if len(arr) > 1:
            chosen = duplicateChoicePrompts(arr)
            path = arr[chosen - 1]
        else:
            path = arr[0]
    else:
        if dst == '.': return os.getcwd()
        path = getOnePath(dst, start)
    return path

def duplicateChoicePrompts(arr):
    click.echo(str(len(arr)) + ' paths found that match your input.\n')
    for dex in range(len(arr)):
        click.echo(str(dex + 1) + ': ' + str(arr[dex]))
    click.echo()
    value = -1
    while value not in range(1, len(arr) + 1):
        value = click.prompt('Enter a path number to proceed ', type=int)
        if value not in range(1, len(arr) + 1):
            click.echo('Error: ' + str(value) + ' is not a valid entry')
    return value

def dealWithResult(path, result):
    if result == 'open-finder':
        if path.split('/')[-1].find('.') > 1:
            click.echo('You input a file. The parent directory has been chosen instead.')
            path = str(('/').join(path.split('/')[:-1]))
        click.echo('Opening the finder now...')
        path = subproccesFormat(path)
        subprocess.Popen(['open', path])
    elif result == 'open-editor':
        click.echo('Opening the text editor now...')
        os.system(editor + ' ' + path)
    else:
        if path.split('/')[-1].find('.') > 1:
            click.echo('You input a file. The parent directory has been chosen instead.')
            path = str(('/').join(path.split('/')[:-1]))
        click.echo('Changing the current working directory now...')
        os.system('cd ' + path + '; /bin/bash')

def getFilePath(fname, path, all=False):
    found = set([])
    for root, dirs, files in os.walk(path):
        if fname in files:
            if all:
                found.add(os.path.join(root, fname))
            else:
                return os.path.join(root, fname)
    return list(found)

def getDirPath(dname, path):
    found = set([])
    home = expanduser("~")
    if os.path.join(home, dname) in paths:
        found.add(os.path.join(home, dname))
    for root, dirs, files in os.walk(path):
        if dname in dirs:
            if all:
                found.add(os.path.join(root, dname))
            else:
                return os.path.join(root, dname)
    return list(found)

def getAllPaths(dst, paths):
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

def getOnePath(dst, paths):
    for startDirectory in paths:
        if dst.find('.') >= 0:
            path = getFilePath(dst, startDirectory)
        else:
            path = getDirPath(dst, startDirectory)

        if path != None and len(path) > 0:
            if type(path) == type([]):
                return formatter(path[0])
            else:
                return formatter(path)

    raise PathError('Path to file/directory not found.')

def subproccesFormat(path):
    ans = ''
    for ch in path:
        if ch == '\\':
            continue
        ans += ch
    return ans

def formatter(path):
    final = ''
    for i in range(len(path) - 1):
        if path[i + 1] == ' ' and path[i] != '\\':
            final += path[i] + '\\'
        else:
            final += path[i]
    return final + path[-1]


# if __name__ == '__main__':
#     cli()