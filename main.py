from src.countries import Country
from src.shipping import calculate_shipping


def print_shipping_costs(country, order_total):
    shipping = calculate_shipping(country, order_total)
    print(f'Shipping cost to {country} for order total £{order_total} is £{shipping}')


if __name__ == '__main__':
    print_shipping_costs(Country.UNITED_KINGDOM.value, 99.99)
    print_shipping_costs(Country.UNITED_KINGDOM.value, 100.00)
    print_shipping_costs(Country.FRANCE.value, 99.99)
    print_shipping_costs(Country.FRANCE.value, 100.00)
    print_shipping_costs(Country.ALBANIA.value, 99.99)
    print_shipping_costs(Country.ALBANIA.value, 100.00)
