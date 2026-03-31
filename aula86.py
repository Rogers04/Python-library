# Dictionary Comprehension and Set Comprehension

product = {
    'name': 'Blue pen',
    'price': 2.5,
    'category': 'Office'
}
'''
dc = {
    key: value.upper()
    if isinstance(value,str) else value
    for key, value
    in product.items()    
}'''

lists = [
    ('a', 'valor a'),
    ('b', 'valor b'),
    ('c', 'valor c'),
]

dc = {
    key: value
    for key, value in lists

}

#print(dict(product))
print(dc)