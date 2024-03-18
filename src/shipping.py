import requests as requests


def get_region(country: str) -> str:
    url = (
        "https://npovmrfcyzu2gu42pmqa7zce6a0zikbf.lambda-url.eu-west-2.on.aws/?country="
        + country
    )
    response = requests.get(url)
    response.raise_for_status()
    return response.json().get("region", "OTHER")


class ShippingCalculator:
    def __init__(
        self, shipping: float, discounted: float = None, threshold: float = None
    ):
        self.shipping = shipping
        self.discounted = discounted
        self.threshold = threshold

    def get_shipping(self, order_total: float) -> float:
        if self.threshold is None:
            return self.shipping
        if order_total < self.threshold:
            return self.shipping
        return self.discounted


SHIPPING_RULES = {
    "UK": ShippingCalculator(shipping=4.99, discounted=0, threshold=100.0),
    "EU": ShippingCalculator(shipping=8.99, discounted=4.99, threshold=100.0),
    "OTHER": ShippingCalculator(shipping=9.99),
}


def calculate_shipping(country: str, order_total: float) -> float:
    return SHIPPING_RULES.get(get_region(country)).get_shipping(order_total)
