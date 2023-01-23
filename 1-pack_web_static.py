#!/usr/bin/python3
"""
generates a .tgz archive from contents
of the web_static folder of AirBnB clone repo
"""
from fabric.api import local
from datetime import datetime


def do_pack():
    """
    return archive path if archive has been correctly generated,
    otherwise, return None
    """
    local("mkdir -p versions")
    path = ("versions/web_static_{}.tgz"
            .format(datetime.strftime(datetime.now(), "%Y%m%d%H%M%S")))
    result = local("tar -czvf {} web_static".format(path))

    if result.failed:
        return None

    return path
