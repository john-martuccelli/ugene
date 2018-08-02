import subprocess
from subprocess import call
call(["vim", "/etc/yum.repos.d/ugene.repo"])
call(['yum', 'clean all'])
call (['yum'], 'info ugene')

