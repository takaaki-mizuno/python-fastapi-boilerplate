import click


@click.group()
def cli():
    pass


@cli.group()
def db():
    pass


@db.group()
def migrate():
    click.echo('Initialized the database')


@cli.command()
@click.option('--host', '-h', default='0.0.0.0', help='hostname')
@click.option('--port', '-p', default='8100', help='port number')
def serve(host: str, port: str):
    import uvicorn
    uvicorn.run(app='app.main:app',
                host=host,
                port=int(port),
                reload=True)


if __name__ == '__main__':
    cli()
