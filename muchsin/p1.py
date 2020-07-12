# By: Jr Budiasto

# Graded #1

def letter_catalog(items, letter='A'):
    pass
    # MULAI KODEMU DI SINI
    return [fruit for fruit in items if fruit.startswith(letter)]


# Graded #2

def counter_item(items):
    pass
    # MULAI KODEMU DI SINI
    return {fruit: items.count(fruit) for fruit in items}


# Graded #3

# dua variable berikut jangan diubah
fruits = ['Apple', 'Avocado', 'Banana', 'Blackberries', 'Blueberries', 'Cherries', 'Date Fruit', 'Grapes', 'Guava',
          'Jackfruit', 'Kiwifruit']
prices = [6, 5, 3, 10, 12, 7, 14, 15, 8, 7, 9]

# list buah
chart = ['Blueberries', 'Blueberries', 'Grapes', 'Apple', 'Apple', 'Apple', 'Blueberries', 'Guava', 'Jackfruit',
         'Blueberries', 'Jackfruit']

# MULAI KODEMU DI SINI
fruit_price = {fruit: prices[idx] for idx, fruit in enumerate(fruits)}


def total_price(dcounter, fprice):
    pass
    # MULAI KODEMU DI SINI
    return sum([fprice[key] * value for key, value in dcounter.items()])


# Graded #4

def discounted_price(total, discount, minprice=100):
    pass
    # MULAI KODEMU DI SINI
    return total - total * discount / 100 if total >= minprice else total


# Graded #5

def print_summary(items, fprice):
    pass
    # MULAI KODEMU DI SINI
    for key, value in sorted(counter_item(items).items()):
        print('{} {} : {}'.format(value, key, fprice[key] * value))

    print('total :', total_price(counter_item(items), fprice))
    print('discount price :', discounted_price(total_price(counter_item(items), fprice), 10, minprice=100))
