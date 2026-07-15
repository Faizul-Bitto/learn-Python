def myFunction():
    print("Inside my function")


myFunction()  #! function calling

print("__________________________")


def printMyName(firstName, lastName):
    print(f"Hello {firstName} {lastName}")


printMyName("John", "Doe")

print("__________________________")


def printColorRed():
    color = "Red"  #! local variable scope
    print(color)


color = "Blue"  #! global variable scope
printColorRed()
print(color)

print("__________________________")


def printNumbers(highestNumber, lowestNumber):
    print(highestNumber, lowestNumber)


printNumbers(lowestNumber=3, highestNumber=10)

print("__________________________")


def multiplyNumbers(a, b):
    return a * b


result = multiplyNumbers(5, 6)
print(result)

print("__________________________")


def printList(list):
    for x in list:
        print(x)


myList = [1, 2, 3, 4, 5]
printList(myList)

print("__________________________")


def totalPriceWithTax(price):
    return price + totalTax(price)


def totalTax(price):
    tax = 0.03
    return price * tax


result = totalPriceWithTax(100)
print(result)
