from setuptools import setup, find_packages

setup(
    name='directorySearch',
    version='1.0.0',
    packages=find_packages(),
    include_package_data=True,
    py_modules=['directorySearch'],
    install_requires=[
        'Click'
    ],
    author='Ben Hubsch',
    description='A command-line program removes the hassle of finding and opening files.',
    url=''
    entry_points='''
        [console_scripts]
        directorySearch=directorySearch:cli
        ...each line here should identify
        ...one console script
        ...the part before the equals sign is the
        ...name of the script that should be generated
        ... and the second part is the import path
        ...followed by a colon with the click command
    '''
)