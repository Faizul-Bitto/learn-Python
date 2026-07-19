# ARGS
def add(*args):
    total = 0
    for arg in args:
        total += arg
    return total


# print(add(1, 2, 3, 4, 5))


def display_name(*args):
    for arg in args:
        print(arg, end=" ")


# display_name("DR.", "Spongebob", "Harold", "Squarepants")


# KWARGS
def print_address(**kwargs):
    for value in kwargs.values():
        print(value)

    for key in kwargs.keys():
        print(key)

    for key, value in kwargs.items():
        print(f"{key} : {value}")


# print_address(street="123", city="Detroit", state="Michigan", zip="54321")


# args and kwargs
def shipping_label(*args, **kwargs):
    for arg in args:
        print(arg, end=" ")
    print()

    for value in kwargs.values():
        print(value, end=" ")
    print()

    for key in kwargs.keys():
        print(key)
    print()

    for key, value in kwargs.items():
        print(f"{key} : {value}")
    print()

    print(f"{kwargs.get('street')}")
    print(f"{kwargs.get('city')}")
    print(f"{kwargs.get('state')}")
    print(f"{kwargs.get('zip')}")


shipping_label(
    "DR.",
    "Spongebob",
    "Harold",
    "Squarepants",
    street="123",
    city="Detroit",
    state="Michigan",
    zip="54321",
)
