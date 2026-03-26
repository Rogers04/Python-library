# List comprehension in Python
# List comprehension is a quick way to create list
# from iterables

#print(list(range(10)))
      

lists = []
for number in range(10):
    lists.append(number)
#print(lists)

lists = [number * 2 
        for number in range(10)
]
print(lists)

# Data mapping in list comprehension 
products = [ 
    {'name': 'p1', 'price': 20, },
    {'name': 'p2', 'price': 10, },
    {'name': 'p3', 'price': 30, },
]

new_products = [
    {**product, 'price': product['price'] * 1.05}
    if product['price'] > 10 else {**product}
    for product in products
]
print(*new_products, sep='\n') 
