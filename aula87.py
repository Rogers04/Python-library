# isinstace - to know if the object is of a certain type
lists = ['a', 1, 1.1, True, [0, 1, 2], (1, 2),
         {0, 1}, {'name': 'Rogers'}]

for item in lists:
    if isinstance(item, set):
        print('SET')
        item.add(5)
        print(item, isinstance(item, set))

    elif isinstance(item, str):
        print('STR')
        print(item.upper(), isinstance(item, set))

    elif isinstance(item, (int, float)):
        print('NUM')
        print(item, item * 2)
    
    else:
        print('OTHERS')
        print(item)