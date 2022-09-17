import typer
from typing import Optional
from beerlog.core import add_beer_to_database, get_beers_from_database

main = typer.Typer(help='Beer Managment Application')


@main.command('add')
def add(
    name: str,
    style: str,
    flavor: int = typer.Option(...),
    image: int = typer.Option(...),
    cost: int = typer.Option(...),
):
    """Adds new beer to database."""
    if add_beer_to_database(name, style, flavor, image, cost):
        print('🍺 beer added to database')
    else:
        print('⛔ there was a problem adding beer to database')


@main.command('list')
def list_beers(style: Optional[str] = None):
    """Lists the beers currently in database"""
    beers = get_beers_from_database()
    print(beers)
