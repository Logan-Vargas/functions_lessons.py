def tea_order(customer_name, tea_type, milk=None):
    print(customer_name, "ordered a", tea_type, "tea")
    if milk!= None:
        print("  - add:", milk, "milk")
tea_order("Alice", "green", "almond")
print(tea_order.__doc__)

print("----------------------------------------------")

def tea_order2(customer_name, tea_type, *args):
    print(customer_name, "ordered a", tea_type, "tea")
    for arg in args:
        print("  - add:", arg)
tea_order2("Bob", "black", "oat", "sugar", "lemon")
print(tea_order2.__doc__)

print("-----------------------------------------------")

def tea_order3(customer_name, tea_type, **kwargs):
    print(customer_name, "ordered a", tea_type, "tea")
    for key, value in kwargs.items():
        print("  -", key + ":", value)
tea_order3("Charlie", "herbal", milk="soy", sweetener="honey", temperature="hot")
print(tea_order3.__doc__)

print("------------------------------------------------")


# Indefinite Arguments (*args) Practice #1
# Create a function called sum_squares that takes any number of numeric arguments, and returns the sum of their values squared. For example for the arguments sum_squares(1,2,3) it should return 14 (1+4+9).
def sum_squares(*args):
    total = 0
    for num in args:
        total += num ** 2
    return total
print(sum_squares(1, 2, 3))
print("------------------------------------------------")
# Indefinite Arguments (*args) Practice #2
# Create a function called absolute_sum, which takes any number of arguments, and returns the sum of their absolute values (that is, it takes the non-negative values and adds them together, in other words, considers them all - negative and positive - as positive).
def absolute_sum(*args):
    total = 0
    for num in args:
        total += abs(num)
    return total
print(absolute_sum(-10, 20, -30, 40))
print("------------------------------------------------")
# Indefinite Arguments (*args) Practice #3
# Create a function called personal_numbers that receives, as its first argument, a name, and then an indefinite number of values.The function should return the following message:"{name}, the sum of your numbers is {sum_numbers}"
def personal_numbers(name, *args):
    sum_numbers = sum(args)
    return f"{name}, the sum of your numbers is {sum_numbers}"
print(personal_numbers("David", 5, 15, 25))
print("------------------------------------------------")