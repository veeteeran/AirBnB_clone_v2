#!/usr/bin/python3
"""Creates and distributes an archive to your web servers
"""
from fabric.state import env
do_pack = __import__('1-pack_web_static').do_pack
do_deploy = __import__('2-do_deploy_web_static').do_deploy

env.user = 'ubuntu'
web01, web02 = '35.190.170.193', '3.80.222.135'
env.hosts = [web01, web02]

def deploy():
    """ do_deploy docstring """
    archive_path = do_pack()
    from os.path import isfile
    if not isfile (archive_path):
        return False
    value = do_deploy(archive_path)
    return value
