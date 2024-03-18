import pytest

from src.countries import Country
from src.shipping import get_region


@pytest.mark.parametrize(
    "country, expected_region",
    [
        (
            Country.UNITED_KINGDOM,
            "UK",
        ),
        (
            Country.FRANCE,
            "EU",
        ),
        (
            Country.ARMENIA,
            "OTHER",
        ),
    ],
)
def test_get_region(country, expected_region):
    region = get_region(country.value)
    assert region == expected_region
