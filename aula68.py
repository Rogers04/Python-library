'''
Function Scope in Python
Scope means the location where that code can reach.
There is global scope and local scope.
Global scope is the scope where all the code is reachable.
Local scope is the scope where only names from the same location
can be reached.
'''


x = 1


def scope():
    global x
    x = 10
    def other_function():
        global x
        x = 11
        y = 2
        print(x, y)


    other_function()
    print(x)




print(x)
scope()
print(x)

