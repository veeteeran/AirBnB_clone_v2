#!/usr/bin/python3
""" Fabric script that generates a .tgz archive
"""
from fabric.api import local
from datetime import datetime


def do_pack():
    """Fabric script that generates a .tgz archive from the contents
    of the web_static folder of your AirBnB Clone repo
    """
    dt = datetime.now()
    dt_format = dt.strftime("%Y-%m-%d %H:%M:%S")
    archive = "web_static_" + dt_format + ".tgz"

    local("mkdir -p ~/AirBnB_clone_v2/versions/")

    try:
        local('tar -cfv {} ~/AirBnB_clone_v2/web_static/'.format(archive))
        path = "~/AirBnB_clone_v2/versions/" + archive
        return path
    except:
        return None
