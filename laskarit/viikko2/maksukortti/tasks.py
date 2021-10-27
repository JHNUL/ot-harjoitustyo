from invoke import task


@task
def test(ctx):
    ctx.run("pytest src --verbose")

@task
def coverage(ctx):
    ctx.run("coverage run --branch -m pytest src")

# will run the task specified in parenthesis first
@task(coverage)
def coverage_report(ctx):
    ctx.run("coverage html")