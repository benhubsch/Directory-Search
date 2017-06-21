# have this module take in the values gathered at installation in setup.py and write them into
# userinfo.py, making them easy to edit after the fact
def writeToFile(paths, editor):
    f = open('userinfo.py', 'w')
    f.write('# paths specified upon install \n')
    f.write('paths = [\'%s\' \n', % paths[0])
    for path in paths[1:-1]:
        f.write('         \'%s\', \n' % path)
    f.write('         \'%s\']  \n \n' % paths[-1])
    f.write('# preferred text editor \n')
    f.write('editor = \'%s\'' % editor)
    f.close()


if __name__ == '__main__':
    writeToFile(['/Users/benhubsch/Desktop/', '/Users/benhubsch/', 'banana', '/Users/benhubsch/Library/Mobile Documents/'], 'atom')
