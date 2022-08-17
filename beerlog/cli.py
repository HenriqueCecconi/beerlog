import typer

main = typer.Typer(help='Beer Managment Application')

@main.command('add')
def add(
    name: str,
    style: str,
    flavor: int = typer.Option(...),
    image: int  = typer.Option(...),
    cost: int   = typer.Option(...),
):
    """Adds new beer to database."""
    print(name, style)

@main.command('list')
def list_beers(style: str):
    """Lists the beers currently in database"""
    print(style)