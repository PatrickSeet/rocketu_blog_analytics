from fabric.colors import green, yellow
from fabric.contrib.files import upload_template
from fabric.decorators import task
from fabric.operations import local
from fabric.api import *

env.hosts = ['54.191.122.152']
env.user = 'ubuntu'
env.key_filename = '~/.ssh/portfolio.pem'
env.shell = "/bin/bash -l -i -c"
env.project_name = "rocketu_blog_analytics"

# @task
# def ubuntu_hello():
#     run("lsb_release -a")

@task
def hello():
    print(green("I'm alive!"))

@task
def create_file(file_name):
    local("touch /Users/Badmuthafucker/Desktop/{}.txt".format(file_name))

@task
def create_dir():
    local("mkdir /Users/Badmuthafucker/Desktop/my_direcotry")

@task
def make_dir(dir_name, path):
    local("mkdir ~/{}/{}".format(dir_name, path))
    # make_dir:/Desktop,test

@task
def ubuntu_hello():
    with hide("stdout"):
        output = run("lsb_release -a")
        print(yellow(output))

@task
def deploy():
    with prefix("workon blog_analytics"):
        with cd("/home/ubuntu/rocketu_blog_analytics"):
            run("git pull origin master")
            run("pip install -r requirements.txt")
            run("python manage.py migrate")
            run("python manage.py collectstatic --noinput")


def restart_app():
    sudo("service supervisor restart")
    sudo("service nginx restart")


@task
def setup_postgres(database_name, password):
    sudo("adduser {}".format(database_name))
    sudo("apt-get install postgresql postgresql-contrib libpq-dev")

    with settings(sudo_user='postgres'):
        sudo("createuser {}".format(database_name))
        sudo("createdb {}".format(database_name))
        alter_user_statement = "ALTER USER {} WITH PASSWORD '{}';".format(database_name, password)
        sudo('psql -c "{}"'.format(alter_user_statement))

@task
def setup_nginx(project_name, server_name):
    upload_template("./deploy/nginx.conf",
                    "/etc/nginx/sites-enabled/{}.conf".format(project_name),
                    {'server_name': server_name},
                    use_sudo=True,
                    backup=False)

    restart_app()


@task
def setup_gunicorn():
    with prefix("workon blog_analytics"):
        with cd("/home/ubuntu/rocketu_blog_analytics"):
            run("pip install gunicorn")
            upload_template("./deploy/gunicorn.conf",
                            "rocketu_blog_analytics/gunicorn.conf",
                {'proc_name': env.project_name},
                use_sudo=True,
                backup=False)

    restart_app()

# @task
# def setup_supervisor():
#     sudo("apt-get install supervisor")
#         with cd("/home/ubuntu/rocketu_blog_analytics"):
#             run("pip install gunicorn")
#             upload_template("./deploy/gunicorn.conf",
#                             "rocketu_blog_analytics/gunicorn.conf",
#                 {'proc_name': env.project_name},
#                 use_sudo=True,
#                 backup=False)
#
#     restart_app()