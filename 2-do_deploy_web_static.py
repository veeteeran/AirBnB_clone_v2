#!/usr/bin/python3
"""Distributes an archive to your web servers,
using the function do_deploy
"""
from fabric.api import env, put, run
env.user = 'ubuntu'
web01, web02 = '35.190.170.193', '3.80.222.135'
env.hosts = [web01, web02]


def do_deploy(archive_path):
    """ do_deploy docstring """
    from os.path import isfile
    if not isfile(archive_path):
        return False

    try:
        # Upload the archive to the /tmp/ directory of the web server
        put(archive_path, "/tmp/")
        #
        archive = archive_path.split('/')[1]
        output = "/data/web_static/releases/{}".format(archive.split('.')[0])
        run("mkdir -p {}/".format(output))
        # Uncompress the archive
        run("tar -xzf /tmp/{} -C {}/".format(archive, output))
        # Delete the archive from the web server
        run("rm -rf /tmp/{}".format(archive))
        run("mv {}/web_static/* {}".format(output, output))
        # Delete the symbolic link
        run("rm -rf /data/web_static/current")
        # Create a new the symbolic link
        run("ln -s {}/ /data/web_static/current".format(output))
        print("New version deployed!")
        return True
    except:
        return False
