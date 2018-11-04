"""Test cases for the UNiDAYS Discounts Programming Challenge."""

from solution import (UnidaysDiscountChallenge,
                      pricing_rules)


test_cases = [
    '',  # None
    'A',
    'B',
    'C',
    'D',
    'E',
    'BB',
    'BBB',
    'BBBB',
    'CCC',
    'CCCC',
    'DD',
    'DDD',
    'EE',
    'EEE',
    'EEEE',
    'DDDDDDDDDDDDDD',
    'BBBBCCC',
    'ABBCCCDDEE',
    'EDCBAEDCBC',
]

expected_results = [
    (0, 0),
    (8, 7),
    (12, 7),
    (4, 7),
    (7, 7),
    (5, 7),
    (20, 7),
    (32, 7),
    (40, 7),
    (10, 7),
    (14, 7),
    (7, 7),
    (14, 7),
    (10, 7),
    (10, 7),
    (15, 7),
    (49, 7),
    (50, 0),
    (55, 0),
    (55, 0),
]


verbose = False


def run():

    for items_list, expected in zip(test_cases, expected_results):
        basket = UnidaysDiscountChallenge(pricing_rules)
        for item in items_list:
            basket.add_to_basket(item)

        price, delivery = basket.calculate_total_price()
        if verbose:
            print('\n\nbasket:')
            print(items_list)
            print('price:', price)
            print('delivery:', delivery)
        if not (price, delivery) == expected:
            raise ValueError('expected {}, got {}'
                             .format(expected, (price, delivery)))

    print('all tests passed!')


run()
