#setup.py
#
import subprocess as s

class InstallError (Exception): pass

try:
    import f2n
except ImportError,e:
    installF2N()
try:
    import astropy.io
except ImportError,e:
    installAstro()

import zipfile,os.path
def unzip(source_filename, dest_dir):
    with zipfile.ZipFile(source_filename) as zf:
        for member in zf.infolist():
            # Path traversal defense copied from
            # http://hg.python.org/cpython/file/tip/Lib/http/server.py#l789
            words = member.filename.split('/')
            path = dest_dir
            for word in words[:-1]:
                drive, word = os.path.splitdrive(word)
                head, word = os.path.split(word)
                if word in (os.curdir, os.pardir, ''): continue
                path = os.path.join(path, word)
            zf.extract(member, path)

def installF2N():
    path = os.path.join(os.getcwd, 'install', 'setup.py')
    code = s.call(['python',path,'install'])
    if (code==0):
        print ("F2N Installed Successfully")
        return
    else:
        InstallError("F2N NOT Installed")
        return

def installAstro():
    url = 'https://github.com/astropy/astropy/archive/master.zip'
    f = urllib2.urlopen(url)
    with open("master.zip", "wb") as code:
    code.write(f.read())
    unzip('master.zip', 'MASTER')
    call = s.call(['python', os.path.join(os.getcwd,'MASTER','setup.py') 'install'])
    if (call==0):
        print ("Astropy Installed Successfully")
        s.call(['rm', '-rf', 'MASTER'])
        return
    else:
        InstallError("Astropy NOT installed successfully")
        return
