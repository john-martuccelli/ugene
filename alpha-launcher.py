import subprocess
from subprocess import call
call(["vim", "/etc/yum.repos.d/ugene.repo"])
write '[ugene]
name=ugene
baseurl=https://raw.githubusercontent.com/jmartuccelli/ugene/master/
enabled=1
gpgcheck=0'
# :x command needed save vim file
call(['yum', 'clean all'])
call (['yum'], 'info ugene')

#not workng yet
#need to write text to vim file then save
