#!/usr/bin/python3
""" module doc
"""
from fabric.api import env, local, put, run, runs_once, task
from datetime import datetime
from os.path import exists, isdir, getsize
env.hosts = ["54.174.3.157", "54.242.203.162"]


@runs_once
def do_pack():
    """generates a tgz archive"""
    try:
        date = datetime.now().strftime("%Y%m%d%H%M%S")
        if isdir("versions") is False:
            local("mkdir versions")
        file_name = "versions/web_static_{}.tgz".format(date)
        print(f'Packing web_static to {file_name}')
        local("tar -cvzf {} web_static".format(file_name))
        print(f'web_static packed: {file_name} -> {getsize(file_name)}Bytes')
        return file_name
    except Exception as ex:
        return None


@task
def do_deploy(archive_path):
    """distributes an archive to the web servers"""
    if exists(archive_path) is False:
        return False
    try:
        file_n = archive_path.split("/")[-1]
        no_ext = file_n.split(".")[0]
        path = "/data/web_static/releases/"
        put(archive_path, '/tmp/')
        run('mkdir -p {}{}/'.format(path, no_ext))
        run('tar -xzf /tmp/{} -C {}{}/'.format(file_n, path, no_ext))
        run('rm /tmp/{}'.format(file_n))
        run('mv {0}{1}/web_static/* {0}{1}/'.format(path, no_ext))
        run('rm -rf {}{}/web_static'.format(path, no_ext))
        run('rm -rf /data/web_static/current')
        run('ln -s {}{}/ /data/web_static/current'.format(path, no_ext))
        return True
    except Exception as ex:
        return False


@task
def deploy():
    """creates and distributes an archive to the web servers"""
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)
