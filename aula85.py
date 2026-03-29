'''
lists = []
    for x in range(3):
        for y in range(3):
            lists.append((x, y))
'''

'''
lists = [
    (x, y)
    for x in range(3)
    for y in range(3)
]
'''

lists = [
    [letter for letter in 'Rogers']
    for y in range(3)
]

print(lists)