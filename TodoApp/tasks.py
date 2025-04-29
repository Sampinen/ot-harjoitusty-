"""Invoke commands you can run in the TodoApp repository. Run Poetry shell command first or write poetry run before the command"""

from invoke import task
from subprocess import call
from sys import platform

@task
def start(ctx):
    """Starts the game"""
    ctx.run("python3 src/main.py", pty=True)

@task
def test(ctx):
    """Runs coverage tests"""
    ctx.run("coverage run --branch -m pytest", pty=True)


@task
def coveragereport(ctx):
    """Returns coverage report"""
    ctx.run("coverage html", pty=True)
    if platform != "win32":
        call(("xdg-open", "htmlcov/index.html"))

@task
def format(ctx):
    """Redefines pylint format"""
    ctx.run("autopep8 --in-place --recursive src", pty=True)

@task
def lint(ctx):
    """Checks the quality of the code"""
    ctx.run("pylint src", pty=True)