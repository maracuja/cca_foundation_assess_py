from src.countries import Country
from src.shipping import calculate_shipping


def print_shipping_costs(country, order_total):
    shipping = calculate_shipping(country, order_total)
    print(f'Shipping cost to {country} for order total £{order_total} is £{shipping}')


if __name__ == '__main__':
    print_shipping_costs(Country.UNITED_KINGDOM.value, 29.99)
    print_shipping_costs(Country.UNITED_KINGDOM.value, 30.00)
    print_shipping_costs(Country.FRANCE.value, 29.99)
    print_shipping_costs(Country.FRANCE.value, 30.00)
    print_shipping_costs(Country.ALBANIA.value, 29.99)
    print_shipping_costs(Country.ALBANIA.value, 30)
