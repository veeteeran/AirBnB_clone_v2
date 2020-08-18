#!/usr/bin/python3
"""Creates and distributes an archive to your web servers
"""
from fabric.api import env


web01, web02 = '35.190.170.193', '3.80.222.135'
env.hosts = [web01, web02]
do_pack = __import__('1-pack_web_static').do_pack
do_deploy = __import__('2-do_deploy_web_static').do_deploy


def deploy():
    """ do_deploy docstring """
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)
