"""
variable scope = where a variable is visible or accessible

scope resolution = LEGB order
Local
Enclosed
Global
Built in


first python will try to find Local variable
if not found, then Enclosed
if not found, then Global
if not found, Built in
"""

#! e is Built-in version of scope resolution
from math import e

a = 100  #! Global Variable, can be accessed anywhere


#! Local Variable
def number1():
    a = 10  #! Local Variable, can't be accessed outside of this function
    print(a)


number1()


#! Enclosed Variable
def number2():
    a = 10  #! Local Variable, this will be taken at second place

    def number3():
        a = 2
        print(a)  #! Enclosed Variable, first this will be taken

    number3()


number2()
