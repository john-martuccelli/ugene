import subprocess
from subprocess import call
##import os to use su?
##su+prompt password not trustworthy
call(["vim", "/etc/yum.repos.d/ugene.repo"])
write '[ugene]
name=ugene
baseurl=https://raw.githubusercontent.com/jmartuccelli/ugene/master/
enabled=1
gpgcheck=0'
# :x command needed save vim file
call(['yum', 'clean all'])
call (['yum'], 'info ugene')

f = open("ugene.repo", "name=ugene")
f.write("baseurl=https://raw.githubusercontent.com/jmartuccelli/ugene/master/")
f.write('enabled=1'
f.write('gpgcheck=0')
