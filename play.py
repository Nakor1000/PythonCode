import re
import bioinformatics
import timemod



class Dog:
    kind = 'canine' # class variable shared by all instances
    ancestor = 'Wolf'
    def __init__(self, name):
        self.name = name    # instance variable unique to each instance
        self.tricks = []
    def addtrick(self, trick):
        self.tricks.append(trick)

h = Dog('Heidy')    
d = Dog('Fido')
e = Dog('Buddy')
print d.kind                  # shared by all dogs
'canine'
print e.kind                  # shared by all dogs
'canine'
print d.name                  # unique to d
'Fido'
print e.name                  # unique to e
'Buddy'
d.addtrick('roll over')
e.addtrick('play dead')
d.addtrick('blackflip')
print d.tricks
print e.tricks
print h.name
h.addtrick("Eat food")
print h.tricks

def fib(n):  # return Fibonacci series up to n
    """Return a list containing the Fibonacci series up to n."""
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)    
        a, b = b, a+b
    return result

print fib(9000)    

timemod.checktime('')

