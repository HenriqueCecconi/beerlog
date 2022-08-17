from typing import Optional
from sqlmodel import SQLModel, Field
from pydantic import validator
from statistics import mean
from datetime import datetime

class Beer(SQLModel, table=True):
    id: Optional[int] = Field(primary_key=True, default=None)
    name: str
    style: str
    flavor: int
    image: int 
    cost: int
    rate: int = 0
    date: datetime = Field(default_factory=datetime.now)

    #cls because this is a class method
    @validator('flavor', 'image', 'cost')
    def validate_ratings(cls, v, field):
        if v < 0 or v > 10:
            #field just have a .name attribute because of the decorator implementing code
            raise RuntimeError(f'{field.name} must be between 1 and 10')
        return v

    @validator('rate', always=True)
    def calculate_rate(cls, v, values):
        rate = mean([values['flavor'],values['image'],values['cost']])
        return int(rate)

brewdog = Beer(name= 'Brewdog', style= 'NEIPA', flavor='5', image='9', cost='10')