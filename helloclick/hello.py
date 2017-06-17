import os
import subprocess
import click

dropbox = '/Users/benhubsch/Dropbox/'
docs = '/Users/benhubsch/Documents/'
downloads = '/Users/benhubsch/Downloads/'
desktop = '/Users/benhubsch/Dropbox/'
general = '/Users/benhubsch/'

@click.command()
@click.option('-d', '--duplicated', is_flag=True, help='To be used when the filename or directory name on your machine is non-unique.')
@click.argument('dst', type=click.Path(), nargs=-1, required=True) # nargs=-1 means that all arguments will be passed as a tuple, no matter how many arguments there are
def cli(dst, duplicated):
    click.echo(duplicated)
    click.echo(dst)
    click.echo(('\ ').join(dst))