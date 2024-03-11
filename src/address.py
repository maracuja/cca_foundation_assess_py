from dataclasses import dataclass
from enum import Enum

from src.countries import Country


@dataclass
class Address:
    house: str
    street: str
    city: str
    postcode: str
    country: Country

