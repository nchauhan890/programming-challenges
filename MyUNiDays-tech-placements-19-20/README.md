## Running the code

To run the code, open 'solution.py' in an IDE supporting python.

To run the tests, open 'tests.py' in an (preferably) interactive Python shell.
The tests will run automatically by importing the code from 'solution.py',
however, you can type `verbose = True` into the shell followed by `run()` to
rerun the tests, but showing the output each time.

## Approach

I began by writing the `UnidaysDiscountsChallenge` class with the 3 methods
`add_to_basket`, `calculate_total_price` and `__init__`. I then set some
attributes in the `__init__` method to hold information like pricing rules
and delivery charges.

After this, I decided to create an `Item` class which could create new
instances which hold data about different items. I also subclassed the basic
class to implement the 3 types of offers:

 - buy x and get y free
 - buy x for the price of y
 - buy x for (£) y

I used subclassing to give me some extensibiity and to reduce my code by using
a particular class twice for different items with the same discount type but
with different discount data (item B and C).

The `self.items` attribute was a dictionary (hash table) which contained the
item name along with its quantity. This would be useful to save time by not
having to calculate quantity inside the `calculate_total_price` method.

Within the `calculate_total_price` method, I looped over each item/quantity
pair, checking which type of item it was:

If the item was an instance of the `XForY` class, I would do the following:

 - use `divmod` to get the number of times the `X` value goes into the
   quantity and how many items are left over
 - price the number of discounted chunks at `Y`
 - price the left over at the standard price of the item

If the item was an instance of the `BuyXGetYFree` class, I would do the
following:

 - calculate the 'chunk' size that would be needed to hold `X + Y`
 - calculate how many items wouldn't fit into the chunk size and remain as
   'left overs'
 - make the rest of the items 'discounted'
 - price the left over items at the standard item price
 - make the discounted items number the proportion of the needed items to the
   chunk size so that the free items aren't charged
 - charge the new discounted number of items at standard price

If the item was an instance of the `XForPriceOfY` class, I would do the
following:

 - calculate the number of items that don't fit into the 'chunk' (`X`) size
 - make the rest of the items 'discounted'
 - price the left over items at the standard item price
 - charge the discounted items at the standard price and multiply this price
   by the fraction of how many items they should be charged for over the number
   of items they are currently being charged for (`Y / X`).

If the previous 3 checks all failed, then the item must be an instance of the
basic `Item` class, therefore:

 - price at the standard item price

Finally, I did a quick check to see whether the cost was less than the delivery
charge limit and more than 0. If so, add the charge on, otherwise keep it as 0.
