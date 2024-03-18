from dataclasses import dataclass

from src.countries import Country


@dataclass
class Address:
    address_id: str
    house: str
    street: str
    city: str
    postcode: str
    country: Country
