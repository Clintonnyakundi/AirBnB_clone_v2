#!/usr/bin/python3
"""
Fabric script (based on the file 1-pack_web_static.py) that distributes
an archive to your web servers,using the function do_deploy
"""
from fabric.api import *
import os

env.hosts = ["100.25.205.123", "100.25.47.49"]
env.user = "ubuntu"


def do_deploy(archive_path):
    """
    distributes an archive to my web servers
    """
    if not os.path.exists(archive_path):
        return False

    upload = put(archive_path, "/tmp/")
    basename = os.path.basename(archive_path)
    if basename[-4:] == ".tgz":
        name = basename[:-4]

    newDir = "/data/web_static/releases/" + name
    run("mkdir -p " + newDir)
    run("tar -xzf /tmp/{} -C {}".format(basename, newDir))

    run("rm /tmp/{}".format(basename))
    run("mv {}/web_static/* {}".format(newDir, newDir))
    run("rm -rf {}/web_static".format(newDir))
    run("rm -rf /data/web_static/current")
    run("ln -s {} /data/web_static/current".format(newDir))

    return True
