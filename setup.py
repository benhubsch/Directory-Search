from setuptools import setup

setup(
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

        # ...each line in entry_points here should identify
        # ...one console script
        # ...the part before the equals sign is the
        # ...name of the script that should be generated
        # ... and the second part is the import path
        # ...followed by a colon with the click command