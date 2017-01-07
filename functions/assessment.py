"""
Skills function assessment.

Please read the the instructions first (separate file). Your solutions should
go below this docstring.

PART ONE: Write your own function declarations - Part 1 questions aren't
included in the doctest.

PART TWO:

    >>> is_berry("blackberry")
    True

    >>> is_berry("durian")
    False

    >>> shipping_cost("blackberry")
    0

    >>> shipping_cost("durian")
    5

    >>> append_to_list([3, 5, 7], 2)
    [3, 5, 7, 2]

    >>> calculate_price(25, "CA")
    27.0

    >>> calculate_price(400, "NM")
    420.0

    >>> calculate_price(150, "OR", 0)
    150

    >>> calculate_price(60, "PA")
    65.0

    >>> calculate_price(38, "MA")
    40.9

    >>> calculate_price(126, "MA")
    135.3

PART THREE: Write your own function declarations - Part 3 questions aren't
included in the doctest.

"""

###############################################################################

# PART ONE

# NOTE: We haven't given you function signatures or docstrings for these, so
# you'll need to write your own. These functions also aren't included in the
# doctests above, so make sure to test them on your own.


#    (a) Write a function that takes a town name as a string and evaluates to
#        `True` if it is your hometown, and `False` otherwise.

def is_my_home_town(town):
    """ 
    function returns True if town entered is my home town"""

    return town == "Atlanta"

#tests:
#print is_my_home_town("Atlanta")
#print is_my_home_town("SF")

#    (b) Write a function that takes a first and last name as arguments and
#        returns the concatenation of the two names in one string.

def combines_firstname_lastname(first_name, last_name):
    """
    Takes first name and last name and concatenates them into one string."""

    return first_name + " " + last_name

#tests:
#print combines_firstname_lastname("Melissa", "Boyer")

#    (c) Write a function that takes a home town, a first name, and a last name
#        as arguments, calls both functions from part (a) and (b) and prints
#        "Hi, 'full name here', we're from the same place!", or "Hi 'full name
#        here', where are you from?" depending on what the function from part
#        (a) evaluates to.

def greets_user(town, first_name, last_name):
    """
    Greets user by name and town.
    Greeting varies if user is from my hometown or from another town"""

    if is_my_home_town(town) == True:
        print "Hi, {} {}, we're from the same place!".format(first_name, last_name)
    else:
        print "Hi, {} {}, where are you from?".format(first_name, last_name)

# Tests:
# greets_user("Atlanta", "Jon", "Snow")
# greets_user("Oakland", "Bob", "Marley")

###############################################################################

# PART TWO

# 1. (a) Write a function, `is_berry()`, which takes a fruit name as a string
#        and returns a boolean if the fruit is a "strawberry", "cherry", or
#        "blackberry."


def is_berry(fruit):
    """Determines if fruit is a berry"""

    if "strawberry" in fruit:
        return True
    if "cherry" in fruit:
        return True
    if "blackberry" in fruit:
        return True
    else:
        return False
    
    #Working to find a less repetitive solution
    # berries = ["strawberry", "cherry", "blackberry"]

    # if berries in fruit:
    #     return True


# (b) Write another function, shipping_cost(), which calculates shipping cost
#     by taking a fruit name as a string and calling the is_berry() function
#     within the shipping_cost() function. Your function should return 0 if
#     is_berry() == True, and 5 if is_berry() == False.

def shipping_cost(fruit):
    """Calculates shipping cost of fruit"""
    if is_berry(fruit) == True:
        return 0
    else:
        return 5


# 2. Make a function that takes in a number and a list of numbers. It should
#    return a new list containing the elements of the input list, along with
#    given number, which should be at the end of the new list.

def append_to_list(lst, num):
    """Creates a new list consisting of the old list with the given number
       added to the end."""

    lst.append(num)
    return lst

#Would the above be more clear if lst was renamed to updated list, even though 
#it's not required to work correctly? The code below works and seems more clear, 
#but the program works either way. Not sure if I'm overthinking it.
    # lst.append(num)
    # updated_list = lst
    # return updated_list


# 3. Write a function calculate_price to calculate an item's total cost by
#    adding tax, and any fees required by state law.

#    Your function will take as parameters (in this order): the base price of
#    the item, a two-letter state abbreviation, and the tax percentage (as a
#    two-digit decimal, so, for instance, 5% will be .05). If the user does not
#    provide a tax rate it should default to 5%.

#    CA law requires stores to collect a 3% recycling fee, PA requires a $2
#    highway safety fee, and in MA, there is a commonwealth fund fee of $1 for
#    items with a base price under $100 and $3 for items $100 or more. Fees are
#    added *after* the tax is calculated.

#    Your function should return the total cost of the item, including tax and
#    fees.




def calculate_price(base_price, state, tax_rate = .05):
    """
    Calculates item price with taxes and fees depending on state."""

    item_with_tax = base_price + (base_price * tax_rate)

    if state == "CA":
        return round(item_with_tax + (item_with_tax * .03), 1) 
    if state == "PA":
        return item_with_tax + 2
    if state == "MA" and base_price < 100:
        return item_with_tax + 1
    if state == "MA" and base_price >= 100:
        return item_with_tax + 3
    else:
        return item_with_tax


#started here, but couldn't get the output formatted correctly for CA
    # print "base price: ", base_price
    # print "tax rate: ", tax_rate
    # print "item_with_tax: ", item_with_tax

    # if state == "CA":
    #     fees = int(item_with_tax) * .03
    # if state == "PA":
    #     fees = 2
    # if state == "MA" and base_price < 100:
    #     fees = 1
    # if state == "MA" and base_price >= 100:
    #     fees = 3
    # if state != "CA" and state != "PA" and state != "MA":
    #     fees = 0
    # total_cost = item_with_tax + fees

    # return total_cost
###############################################################################

# PART THREE: ADVANCED

# NOTE: We haven't given you function signatures and docstrings for these, so
# you'll need to write your own. These functions also aren't included in the
# doctests above, so make sure to test them on your own.


# 1. Make a new function that takes in a list and any number of additional
# arguments, appends them to the list, and returns the entire list. Hint: this
# isn't something we've discussed yet in class; you might need to google how to
# write a Python function that takes in an arbitrary number of arguments.

def adds_unknown_number_of_items_to_list(lst, *args):
    """
    Adds an unknown number of items to the end of list lst"""
    for arg in args:
        lst.append(arg)
    return lst

#tests:
# numbers = [1, 2, 3, 4]
# print adds_unknown_number_of_items_to_list(numbers, 1, 2, 3)


# 2. Make a new function with a nested inner function.
# The outer function will take in a word.
# The inner function will multiply that word by 3.
# Then, the outer function will call the inner function.
# Output will be the original function argument and the result of the inner
# function.

# Example:

#>>> outer("Balloonicorn")
#('Balloonicorn', 'BalloonicornBalloonicornBalloonicorn')

def prints_word_three_times(word): 
    """
    Prints the input word once and then three times"""
    result = ''
    def multiply_by_3(word):
        return word * 3

    return word, multiply_by_3(word)

#tests
#print prints_word_three_times("hello")

###############################################################################

# END OF ASSESSMENT: You can ignore everything below.

if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GOOD WORK!"
    print
