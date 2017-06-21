

def writeToFile(paths, editor):
    f = open('userinfo.py', 'w')
    f.write('# paths specified upon install \n')
    f.write('paths = [\'%s\' \n' % paths[0])
    for path in paths[1:-1]:
        f.write('         \'%s\', \n' % path)
    f.write('         \'%s\']  \n \n' % paths[-1])
    f.write('# preferred text editor \n')
    f.write('editor = \'%s\'' % editor)
    f.close()
