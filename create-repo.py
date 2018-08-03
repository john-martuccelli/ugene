import subprocess
from subprocess import call
#reqirement run as root user
f = open("ugene.repo /etc/yum.repos.d/", "w")
f.write ('[ugene]')
f.write ('name=ugene')
f.write ("baseurl=https://raw.githubusercontent.com/jmartuccelli/ugene/master/")
f.write ('enabled=1')
f.write ('gpgcheck=0')
sys.exit()

#useless
#thanks jbieren for the aneurysm
