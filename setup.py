from setuptools import setup
import click
import os
from os.path import expanduser, isdir
import time
import distutils.cmd
import setuptools.command.build_py



class InstallCommand(distutils.cmd.Command):
    description = "Takes in user input needed to properly setup."
    user_options = [
        ('file-paths=', 'f', 'Specify the file paths you\'d like to add.'),
        ('text-editor=', 't', 'Specify the text editor you\'d like to use.'),
    ]
    def initialize_options(self):
        self.file_paths = []
        self.text_editor = 'open'
    def finalize_options(self):
        home = expanduser("~")
        for standard in ['Documents', 'Desktop', 'Downloads']:
            currentPath = home + '/' + standard
            if os.path.isdir(currentPath):
                self.file_paths.append(currentPath)

    def run(self):
        home = expanduser("~")
        dbox = click.prompt('Do you use Dropbox? (y/n)')
        while dbox != 'y' and dbox != 'n':
            click.echo('\'y\' or \'n\' are the only valid responses')
            dbox = click.prompt('Do you use Dropbox? (y/n)')
        if dbox == 'y':
            dboxPath = home + '/' + 'Dropbox'
            if os.path.isdir(dboxPath):
                self.file_paths.append(dboxPath)
            else:
                click.echo('We couldn\'t find if/where you have your Dropbox stored as a directory on your computer. You can enter the path manually in a moment.')
                time.sleep(2)

        icloud = click.prompt('Do you use iCloud? (y/n)')
        while icloud != 'y' and icloud != 'n':
            click.echo('\'y\' or \'n\' are the only valid responses')
            icloud = click.prompt('Do you use iCloud? (y/n)')
        if icloud == 'y':
            click.echo('iCloud is a bit a pain in that there\'s no top level directory that can be easily scanned for file and directory names. I haven\'t yet found a good solution to this--if anyone thinks of one I\'d love to hear it.')
            icloudPath = home + '/Library/Mobile\ Documents/'
            # click.echo(icloudPath)
            # if os.path.isdir(icloudPath):  # .isdir vs. .exists(path) ???
            #     self.file_paths.append(icloudPath)
            # else:
            #     click.echo('We couldn\'t find if/where you have your iCloud stored as a directory on your computer. You can enter the path manually in a moment.')
                # time.sleep(2)
            time.sleep(2)

        # def getPreferredPaths(self.file_paths):
        preferred = []
        click.echo('\nThe following paths have already been added to the search path and will be searched by default: \n')
        for item in self.file_paths:
            click.echo(item)
        click.echo('\n')
        click.echo('If there are other directories that you use with frequency besides those, it is highly recommended that you add their paths now. You can also add them later manually in userinfo.py. If you are done entering paths at any point, simply type the word \'done\'. ')
        value = click.prompt('Enter a path here (optional)')
        while value != 'done':
            if os.path.isdir(value):
                preferred.add(value)
            else:
                click.echo('That was not recognized by your operating system as a valid path to a directory. Note: if you have directory names that are more than two words, you may have to escape the space manually, i.e. \'Example Directory\' --> \'Example\\ Directory\'. If you are done entering paths at any point, simply type the word \'done\'.')
            value = click.prompt('Enter a path here (optional)')
        click.echo('\n \n')
        self.file_paths.extend(preferred)

        #deg getEditor():
        click.clear()
        click.echo('Last step of installation! This is your chance to specify a preferred text editor. Editors currently supported include Atom, Sublime, and Visual Studio Code. If you don\'t specify, files will be opened according to their default application settings.\n')
        click.echo('1: Atom')
        click.echo('2: Sublime')
        click.echo('3: Visual Studio Code')
        click.echo('4: None (open files with default application)')
        value = click.prompt('Enter the number corresponding to your choice here', type=int)
        while value not in [1, 2, 3, 4]:
            click.echo(str(value) + ' is not a valid choice.')
            value = click.prompt('Enter the number corresponding to your choice here', type=int)
        click.echo('\n')
        if value == 1:
            click.echo('If you haven\'t already, be sure to select \'Atom\' -> \'Install Shell Commands\' for this program to work using the command line.')
        elif value == 2:
            click.echo('If Sublime isn\'t already set up to work using the command line, follow the steps at the following link to get set up: https://www.sublimetext.com/docs/3/osx_command_line.html.')
        elif value == 3:
            click.echo('If Visual Studio Code isn\'t already set up to work using the command line, follow the steps at the following link to get set up: https://code.visualstudio.com/docs/setup/mac.')
        editor = ['atom', 'subl', 'code', 'open'][value - 1]


        click.echo('\nYou\'re all set up now! Type \'ff --help\' to see what you can do with this program.')


        # def writeToFile(paths, editor):
        f = open('userinfo.py', 'w')
        f.write('# paths specified upon install \n')
        f.write('paths = [\'%s\' \n' % self.file_paths[0])
        for path in self.file_paths[1:-1]:
            f.write('         \'%s\', \n' % path)
        f.write('         \'%s\']  \n \n' % self.file_paths[-1])
        f.write('# preferred text editor \n')
        f.write('editor = \'%s\'' % editor)
        f.close()

class BuildCommand(setuptools.command.build_py.build_py):
  def run(self):
    self.run_command('install')
    setuptools.command.build_py.build_py.run(self)


if __name__ == '__main__':
    setup(
        # cmdclass={
        #     'install': InstallCommand,
        #     'build_py': BuildCommand,
        # },
        name='File Finder',
        version='1.0',
        py_modules=['fileFind'],
        install_requires=[
            'Click',
        ],
        author='Ben Hubsch',
        description='A command-line program removes the hassle of finding and opening files.',
        url='https://github.com/benhubsch/File-Finder',
        entry_points='''
            [console_scripts]
            ff=fileFind:cli
        '''
    )

