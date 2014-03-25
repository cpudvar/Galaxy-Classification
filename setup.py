#setup.py
#Installs f2n, Astropy, and PIL

import os.path
import subprocess as s
import tarfile
import urllib2
import zipfile

class InstallError (Exception): pass

try:
    import f2n
except ImportError,e:
    installF2N()
try:
    import astropy.io
except ImportError,e:
    installAstro()
try:
    import PIL
except ImportError,e:
    installPIL()

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

#Needed to convert FITS to PNG for viewing
def installF2N():
    path = os.path.join(os.getcwd, 'install', 'setup.py')
    code = s.call(['python',path,'install'])
    if (code==0):
        print ("F2N Installed Successfully")
    else:
        InstallError("F2N NOT Installed")
    return

#Needed to run program
def installAstro():
    url = 'https://github.com/astropy/astropy/archive/'
    filename = 'master.zip'
    f = urllib2.urlopen(url+filename)
    with open(filename, "wb") as code:
    code.write(f.read())

    unzip(filename, 'MASTER')
    call = s.call(['python', os.path.join(os.getcwd(),'MASTER','astropy-master','astropy-master','setup.py') 'install'])
    if (call==0):
        print ("Astropy Installed Successfully")
        s.call(['rm', '-rf', 'MASTER'])
    else:
        InstallError("Astropy NOT installed successfully")
    return

#Needed by f2n
def installPIL():
    url = 'http://effbot.org/downloads/'
    filename = 'Imaging-1.1.7.tar.gz'
    f = urllib2.urlopen(url+filename)
    with open(filename, "wb") as code:
        code.write(f.read())

    tfile = tarfile.open(filename, 'r:gz')
    tfile.extractall('.')
    tfile.close()
    call = s.call(['python', os.path.join(os.getcwd(),filename[:-7],'setup.py') 'install'])
    if (call==0):
        print ("PIL Installed Successfully")
        ret = s.call(['rm', '-rf', filename[:-7])
        if (ret==0):
    else:
        InstallError("PIL NOT installed successfully")
    return
