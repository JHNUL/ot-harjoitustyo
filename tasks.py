from invoke import task


@task
def test(ctx):
    ctx.run('ENV=test pytest ./src')


@task
def start(ctx):
    ctx.run('ENV=prod python3 ./src/index.py')


@task
def coverage(ctx):
    ctx.run('ENV=test coverage run --branch -m pytest ./src')


@task(coverage)
def coverage_report(ctx):
    ctx.run('coverage html')
