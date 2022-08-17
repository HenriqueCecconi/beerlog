from typing import Optional, List
from sqlmodel import Session, create_engine
from beerlog.database import get_session
from beerlog.models import Beer

def add_beer_to_database(
    name:   str,
    style:  str,
    flavor: int,
    image:  int,
    cost:   int,
) -> bool:
    with get_session() as session:
        beer = Beer(
            name   = name,
            style  = style,
            flavor = flavor,
            image  = image,
            cost   = cost
        )
        session.add(beer)

    return True