# funtion = A block of reusable code 
#           Place () after the function name when you call it

def happy_birthday(name, age):
    print(f"Happy Birthday to you {name}!")
    print(f"You are {age} old!")
    print("Happy Birthday to you!")
    print()

happy_birthday("Bro", 21)
happy_birthday("Sis", 18)
happy_birthday("Mom", 45)


def display_invoice(username, amount, due_date):
    print(f"Hello {username},")
    print(f"Your invoice amount is ${amount}is due: {due_date}")
    print("Thank you for your business!")
    print()

display_invoice("Alice", 250.75, "2024-07-15")
display_invoice("Bob", 100.00, "2024-08-01")
display_invoice("Charlie", 300.50, "2024-09-10")


#return = statement used to end a funtion and send a result back to the caller
def add(x, y):
    z  = x + y
    return z

def subtract(x, y):
    z = x - y
    return z

def multiply(x, y):
    z = x * y
    return z   

def divide(x, y):
    z = x / y
    return z

def create_name(first_name, last_name):
    first = first_name.capitalize()
    last = last_name.capitalize()
    return first + " " + last

full_name = create_name("john", "doe")
print(full_name)

# Methods, Help & Documentation Practice #1
# Remove the characters to the left of our main text:

# ,

# :

# %

# _

# #

# Use the lstrip() method. Print the result to the screen:

# ",:_#,,,,,,:::____##Total_ _Pyt%on,,,,,,::#"

# Search the documentation for the requested method to learn how it works. You can use intermediate variables if you need them.


# Methods, Help & Documentation Practice #2
# Add the element "orange" as the fourth element of the following list fruits, using the insert() method:

# fruits = ["mango", "banana", "cherry", "plum", "grapefruit"]

# Search the documentation for the requested method to know how it works.

# Methods, Help & Documentation Practice #3
# Check if the sets below are isolated (that is, they have no elements in common), using the isdisjoint() method. Store this result in the isolated_sets variable:

# phone_brands = {"Samsung", "Xiaomi", "Apple", "Huawei", "LG"}
# tv_brands = {"Sony", "Philips", "Samsung", "LG"}
# Search the documentation for the requested method to know how it works.

