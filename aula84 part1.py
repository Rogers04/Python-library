    # List comprehension in Python
# List comprehension is a quick way to create list
# from iterables

#print(list(range(10))
      

lists = []
for number in range(10):
    lists.append(number)
#print(lists)

lists = [number * 2 
        for number in range(10)
]
print(lists)