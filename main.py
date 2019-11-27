import click


@click.group()
def cli():
    pass


@cli.command('test')
@click.option('--count', default=1, help='Number of times to greet')
def say_hi(count):
    for _ in range(count):
        print('Hi')


if __name__ == '__main__':
    cli()
