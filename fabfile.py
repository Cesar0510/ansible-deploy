



from fabric.api import env, run 
from fabric.api import local 


env.user = 'ubuntu'
env.hosts = ['165.227.159.75']
env.key_filename = '/home/cesar/.ssh/cahedenez_lenovo'


def host():
    run('uname -u')
    
