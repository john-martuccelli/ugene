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

##yum install ugene

#not workng yet
#need to write text to vim file then save
#might be more efficient if people just create the vim file,
#it is easier, 
#if people cant do it thats a bad sign
