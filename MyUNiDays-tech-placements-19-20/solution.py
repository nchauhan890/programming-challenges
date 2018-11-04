"""UNiDAYS Discounts Progamming Challenge."""


class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        # every item must have an item name and base price


class XForY(Item):
    def __init__(self, name, price, x, y):
        super(XForY, self).__init__(name, price)
        self.x = x
        self.y = y


class BuyXGetYFree(Item):
    def __init__(self, name, price, x, y):
        super(BuyXGetYFree, self).__init__(name, price)
        self.x = x
        self.y = y


class XForPriceOfY(Item):
    def __init__(self, name, price, x, y):
        super(XForPriceOfY, self).__init__(name, price)
        self.x = x
        self.y = y


A, B, C, D, E = 'A', 'B', 'C', 'D', 'E'
# create some aliases for the items


class UnidaysDiscountChallenge:
    def __init__(self, pricing_rules, delivery_charge=7, delivery_limit=50):
        self.pricing_rules = pricing_rules
        self.items = {item: 0
                      for item in pricing_rules.keys()}
        self.delivery_charge = delivery_charge
        self.delivery_limit = delivery_limit

    def add_to_basket(self, item):
        try:
            self.items[item] += 1
        except KeyError:
            print('invalid item {}'.format(item))

    def calculate_total_price(self):
        total = 0
        for name, quantity in self.items.items():
            pricing = self.pricing_rules[name]

            if isinstance(pricing, XForY):
                discounted, normal = divmod(quantity, pricing.x)
                total += discounted * pricing.y
                # the discounted multiples are priced with the 'y' price
                total += normal * pricing.price
                # the rest of the items are priced normally

            elif isinstance(pricing, BuyXGetYFree):
                multiple = pricing.x + pricing.y
                # the chunks that will be counted: 'buy 2 get 1 free'
                # would be counted in chunks of 3 (1 + 2)
                leftover = quantity % multiple
                # the items that don't fill a full chunk
                discounted = quantity - leftover
                # the items that do fit into a chunk

                total += leftover * pricing.price
                # the ones that aren't counted are priced normally
                total += discounted * (pricing.x / (multiple)) * pricing.price
                # the number of discounted items is altered so that the
                # items that are given 'free' are taken out. In 'buy 2
                # get 1 free', 2/3 are left over as the 1/3 is given free.
                # the 1/3 is actually 1/(2+1).

            elif isinstance(pricing, XForPriceOfY):
                leftover = quantity % pricing.x
                # the number of items that don't fill the last 'chunk'
                discounted = quantity - leftover
                # the items that do fit into the 'chunks'

                total += leftover * pricing.price
                # the leftover items are priced normally
                total += discounted * (pricing.y / pricing.x) * pricing.price
                # the discounted ones are priced normally, then altered
                # so that the actual price is the price that is given in
                # the deal (pricing.y)

            else:
                total += quantity * pricing.price

        if 0 < total < self.delivery_limit:
            delivery = self.delivery_charge
            # add the delivery charge if under the limit
            # (but only if there are actually any items)
        else:
            delivery = 0
        return total, delivery


pricing_rules = {
    A: Item(A, 8),
    B: XForY(B, 12, 2, 20),
    C: XForY(C, 4, 3, 10),
    D: BuyXGetYFree(D, 7, 1, 1),
    E: XForPriceOfY(E, 5, 3, 2)
}
# initialise items with pricing rules

basket = UnidaysDiscountChallenge(pricing_rules)
# initialise basket

basket.add_to_basket(A)
basket.add_to_basket(D)
