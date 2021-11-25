from invoke import task


@task
def test(ctx):
    ctx.run('ENV=test pytest -s ./src')


@task
def start(ctx):
    ctx.run('ENV=prod python3 ./src/index.py')


@task
def coverage(ctx):
    ctx.run('ENV=test coverage run --branch -m pytest ./src')


@task(coverage)
def coverage_report(ctx):
    ctx.run('coverage html')


@task
def lint(ctx):
    ctx.run('pylint src')


@task
def prettify(ctx):
    ctx.run('autopep8 --in-place --recursive src')
