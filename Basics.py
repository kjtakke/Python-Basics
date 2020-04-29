# Screen Resolution 1400 x 900
# DATA TYPES
# Set Dynamiclly
x01 = "Hello World"  # str
x02 = 20  # int
x03 = 20.5  # float
x04 = 1j  # complex
x05 = ["apple", "banana", "cherry"]  # list
x06 = ("apple", "banana", "cherry")  # tuple
x07 = range(6)  # range
x08 = {"name": "John", "age": 36}  # dict
x09 = {"apple", "banana", "cherry"}  # set
x10 = frozenset({"apple", "banana", "cherry"})  # frozenset
x11 = True  # bool
x12 = b"Hello"  # bytes
x13 = bytearray(5)  # bytearray
x14 = memoryview(bytes(5))  # memoryview

# print(type(x12))



# Casting/Explicit
y01 = str(1)
y02 = int(1)
y03 = float(1)
y04 = complex(1j)
y05 = list(["apple", "banana", "cherry"])
y06 = tuple(("apple", "banana", "cherry"))
y07 = range(6)
y08 = dict({"name": "John", "age": 36})
y09 = set({"apple", "banana", "cherry"})
y10 = frozenset({"apple", "banana", "cherry"})
y11 = bool(True)
y12 = bytes(b"Hello")
y13 = bytearray(5)
y14 = memoryview(bytes(5))

# print(type(y12))
# ________________________________________________________________
# example
a01 = float(1)  # a01 will be 1.0
a02 = float(2.8)  # a02 will be 2.8
a03 = float("3")  # a03 will be 3.0
a04 = float("4.2")  # a04 w will be 4.2

# Number Types
z01 = 5.2       #float
z02 = 2         #int
z03 = 3 + 5j    #complex

    #complex numbers
    # Python code to demonstrate the working of
    # complex(), real() and imag()

    # importing "cmath" for complex number operations

import cmath
# Initializing real numbers
x = 5
y = 3

# converting x and y into complex number
z = complex(x, y)

# printing real and imaginary part of complex number

#print(z.real)
#print(z.imag)
#print(cmath.polar(z))               #Return the representation of x in polar coordinates. Returns a pair (r, phi) where r is the modulus of x and phi is the phase of x.
#print(z == z.real + z.imag * 1j)    #i in math j in python -- j = square root of -1 one
#print(z)




# print(z01 + z02 + z03)

# Strings__________________________________________________
# print(str(a01) + "hello")
# print(str(a01), "hello")    #the "," adds a space

a06 = " Hello, World! "
# print(a06[1])
# print(a06[2:5])
# print(a06[-5:-2])
# print(len(a06))
# print(a06.strip())
# print(a06.lower())
# print(a06.upper())
# print(a06.replace("H", "J"))
# print(a06.split(",")) # returns ['Hello', ' World!']
q01 = "Hell" in a06
# print(q01)

a07 = "Hello"
a08 = "World"
a09 = a07 + " " + a08
# print(a09)
a10 = a07, a08
# print(a10)


# a11 = input("Name: ")
# a12 = input("Your Age: ")
# a13 = "My name is " + a11  + ", I am " + str(a12)
# print(a13)


# print("'''''''")
# print('""""""""""')

# Code	Result	Try it
# \'	Single Quote
# \\	Backslash
# \n	New Line
# \r	Carriage Return
# \t	Tab
# \b	Backspace
# \f	Form Feed
# \ooo	Octal value
# \xhh	Hex value

# print(" \'   \\   \n    \r   \t    \b   \f ")
# print("\110\145\154\154\157")
# print("\x48\x65\x6c\x6c\x6f")

#   capitalize()	Converts the first character to upper case
#   casefold()	Converts string into lower case
#   center()	Returns a centered string
#   count()	Returns the number of times a specified value occurs in a string
#   encode()	Returns an encoded version of the string
#   endswith()	Returns true if the string ends with the specified value
#   expandtabs()	Sets the tab size of the string
#   find()	Searches the string for a specified value and returns the position of where it was found
#   format()	Formats specified values in a string
#   format_map()	Formats specified values in a string
#   index()	Searches the string for a specified value and returns the position of where it was found
#   isalnum()	Returns True if all characters in the string are alphanumeric
#   isalpha()	Returns True if all characters in the string are in the alphabet
#   isdecimal()	Returns True if all characters in the string are decimals
#   isdigit()	Returns True if all characters in the string are digits
#   isidentifier()	Returns True if the string is an identifier
#   islower()	Returns True if all characters in the string are lower case
#   isnumeric()	Returns True if all characters in the string are numeric
#   isprintable()	Returns True if all characters in the string are printable
#   isspace()	Returns True if all characters in the string are whitespaces
#   istitle()	Returns True if the string follows the rules of a title
#   isupper()	Returns True if all characters in the string are upper case
#   join()	Joins the elements of an iterable to the end of the string
#   ljust()	Returns a left justified version of the string
#   lower()	Converts a string into lower case
#   lstrip()	Returns a left trim version of the string
#   maketrans()	Returns a translation table to be used in translations
#   partition()	Returns a tuple where the string is parted into three parts
#   replace()	Returns a string where a specified value is replaced with a specified value
#   rfind()	Searches the string for a specified value and returns the last position of where it was found
#   rindex()	Searches the string for a specified value and returns the last position of where it was found
#   rjust()	Returns a right justified version of the string
#   rpartition()	Returns a tuple where the string is parted into three parts
#   rsplit()	Splits the string at the specified separator, and returns a list
#   rstrip()	Returns a right trim version of the string
#   split()	Splits the string at the specified separator, and returns a list
#   splitlines()	Splits the string at line breaks and returns a list
#   startswith()	Returns true if the string starts with the specified value
#   strip()	Returns a trimmed version of the string
#   swapcase()	Swaps cases, lower case becomes upper case and vice versa
#   title()	Converts the first character of each word to upper case
#   translate()	Returns a translated string
#   upper()	Converts a string into upper case
#   zfill()	Fills the string with a specified number of 0 values at the beginning


# ____________________________________________________________________
# Booleans
# print(10 > 9)
# print(10 == 9)
# print(10 < 9)


# OPERATORS___________________________________________________________
# Arithmetic operators are used with numeric values to perform common mathematical operations:

#    Operator	Name	        Example
#    +	        Addition	    x + y
#    -	        Subtraction	    x - y
#    *	        Multiplication	x * y
#    /	        Division	    x / y
#    %	        Modulus	        x % y
#    **	        Exponentiation	x ** y
#    //	        Floor division	x // y


# Assignment Operators_______________________________________________
# Assignment operators are used to assign values to variables:

#    Operator	Example	    Same As
#    =	        x = 5	    x = 5
#    +=	        x += 3	    x = x + 3
#    -=	        x -= 3	    x = x - 3
#    *=	        x *= 3	    x = x * 3
#    /=	        x /= 3	    x = x / 3
#    %=	        x %= 3	    x = x % 3
#    //=	    x //= 3	    x = x // 3
#    **=	    x **= 3	    x = x ** 3
#    &=	        x &= 3	    x = x & 3
#    |=	        x |= 3	    x = x | 3
#    ^=	        x ^= 3	    x = x ^ 3
#    >>=	    x >>= 3	    x = x >> 3
#    <<=	    x <<= 3	    x = x << 3


# Comparison Operators_______________________________________________
# Comparison operators are used to compare two values:

#    Operator	    Name	                    Example
#    ==	            Equal	                    x == y
#    !=	            Not equal	                x != y
#    >	            Greater than	            x > y
#    <	            Less than	                x < y
#    >=	            Greater than or equal to	x >= y
#    <=	            Less than or equal to	    x <= y


# Logical Operators___________________________________________________
# Logical operators are used to combine conditional statements:

#    Operator	Description	                                                Example
#    and 	    Returns True if both statements are true	                x < 5 and  x < 10
#    or	        Returns True if one of the statements is true               x < 5 or x < 4
#    not	    Reverse the result, returns False if the result is true	    not(x < 5 and x < 10)


# Identity Operators__________________________________________________
# Identity operators are used to compare the objects, not if they are equal,
# but if they are actually the same object, with the same memory location:

#    Operator	Description	                                                Example
#    is 	        Returns True if both variables are the same object	    x is y
#    is not	    Returns True if both variables are not the same object	    x is not y


# Membership Operators_________________________________________________
# Membership operators are used to test if a sequence is presented in an object:
#    Operator	Description	                                                                        Example
#    in 	    Returns True if a sequence with the specified value is present in the object	    x in y
#    not in	    Returns True if a sequence with the specified value is not present in the object	x not in y


# Bitwise Operators_____________________________________________________
# Bitwise operators are used to compare (binary) numbers:
#    Operator	Name	                Description
#    & 	        AND	                    Sets each bit to 1 if both bits are 1
#    |	        OR	                    Sets each bit to 1 if one of two bits is 1
#    ^	        XOR	                    Sets each bit to 1 if only one of two bits is 1
#    ~ 	        NOT	                    Inverts all the bits
#    <<	        Zero fill left shift	Shift left by pushing zeros in from the right and let
# the leftmost bits fall off
#    >>	        Signed right shift	    Shift right by pushing copies of the leftmost bit in from
# the left, and let the rightmost bits fall off


# Lists_________________________________________________________________
mylist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(mylist)
# print(mylist[1])
# print(mylist[-1])
# print(mylist[2:5])
# print(mylist[:4])
# print(mylist[2:])
# print(mylist[-4:-1])

mylist[1] = "blackcurrant"
# print(mylist)

mylist.append("lemon")
# print(mylist)

mylist.remove("orange")
# print(mylist)

mylist.pop(0)
# print(mylist)

del mylist[0]
# print(list)

mylist1 = mylist.copy()
# print(mylist1)

mylist1 = mylist
# print(mylist1)

mylist.clear()
# print(mylist)

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list3 = list1 + list2
# print(list3)

for x in list2:
    list1.append(x)
# print(list1)

list1.extend(list2)
# print(list1)


# Tuple_________________________________________________________________
# A tuple is a collection which is ordered and unchangeable.

tuple = ("apple", "banana", "cherry")
# print(tuple)

# print(tuple[1])

# Convert to list
newlist = []
for x in tuple:
    newlist.append(x)
# print(newlist)


# Sets__________________________________________________________________
# A set is a collection which is unordered and unindexed. In Python sets are written with curly brackets.

set = {"apple", "banana", "cherry"}
# print(set)
# print("banana" in set)

# for x in set:
# print(x)

set.add("orange")
# print(set)

set.remove("banana")
set.discard("banana")
set.clear()
del set

# Dictionary__________________________________________________________
# A dictionary is a collection which is unordered, changeable and indexed.
# In Python dictionaries are written with curly brackets, and they have keys and values.

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
# print(thisdict)
# print(thisdict["model"])

# print(thisdict.get("year"))

# thisdict["year"] = 2018
# print(thisdict.get("year"))

# if "model" in thisdict:
# print("Yes, 'model' is one of the keys in the thisdict dictionary")

thisdict["color"] = "red"
# print(thisdict)

thisdict.pop("model")
# print(thisdict)



import pandas as pd

test_string = "Uh, oh, many, many, many nights go by, I sit alone at home and I cry over you. What can I do. Can't help myself, 'cause baby, it's you. Baby, it's you."

test_string = test_string.lower()
#print (test_string)

res = test_string.split()

#print (str(res))

def word_freq(string):
    mydict = {}
    for word in string:
        if word in mydict:
            mydict[word] += 1
        else:
            mydict[word] = 1
    return mydict

#print(word_freq(res))











# Dates_______________________________________________________________
import datetime

# print(datetime.datetime.now())
x = datetime.datetime.now()
# print(x)
# print(x.strftime("%m/%d/%Y, %H:%M:%S"))
x = datetime.datetime(2019, 1, 1)
# print(x)


#    Directive   Description	                                                    Example
#    %a	        Weekday, short version	                                        Wed
#    %A	        Weekday, full version	                                        Wednesday
#    %w	        Weekday as a number 0-6, 0 is Sunday	                        3
#    %d	        Day of month 01-31	                                            31
#    %b	        Month name, short version	                                    Dec
#    %B	        Month name, full version	                                    December
#    %m	        Month as a number 01-12	                                        12
#    %y	        Year, short version, without century	                        18
#    %Y	        Year, full version	                                            2018
#    %H	        Hour 00-23	                                                    17
#    %I	        Hour 00-12	                                                    05
#    %p	        AM/PM	                                                        PM
#    %M	        Minute 00-59	                                                41
#    %S	        Second 00-59	                                                08
#    %f	        Microsecond 000000-999999	                                    548513
#    %z	        UTC offset	                                                    +0100
#    %Z	        Timezone	                                                    CST
#    %j	        Day number of year 001-366	                                    365
#    %U	        Week number of year, Sunday as the first day of week, 00-53	    52
#    %W	        Week number of year, Monday as the first day of week, 00-53	    52
#    %c	        Local version of date and time	                                Mon Dec 31 17:41:00 2018
#    %x	        Local version of date	                                        12/31/18
#    %X	        Local version of time	                                        17:41:00
#    %%	        A % character	%


# Logic Statments_____________________________________________________
a = 33
b = 33

# if a == b: print("a is greater than b")

# if b > a:
# print("b is greater than a")
# elif a == b:
# print("a and b are equal")
# else:
# print("b is less than a")


a = 200
b = 33
c = 500

# if a > b and c > a:
# print("Both conditions are True")


a = 200
b = 33
c = 500
# if a > b or a > c:
# print("At least one of the conditions is True")


x = 41

# if x > 10:
# print("Above ten,")
# if x > 20:
# print("and also above 20!")
# else:
# print("but not above 20.")

if b > a:
    pass

# Loops______________________________________________________________
# While Loop

i = 1
while i < 6:
    # print(i)
    i += 1

i = 1
while i < 6:
    # print(i)
    if i == 3:
        break
    i += 1

i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    # print(i)

    # For Loop

fruits = ["apple", "banana", "cherry"]
# for x in fruits:
# print(x)

# for x in "banana":
# print(x)

# for x in range(6):
# print(x)

# for x in range(2, 30):
# print(x)

# Increment the sequence with 3 (default is 1):
# for x in range(2, 30, 3):
# print(x)


# adj = ["red", "big", "tasty"]
# fruits = ["apple", "banana", "cherry"]

# for x in adj:
# for y in fruits:
# print(x, y)


# Arrays_____________________________________________________________
import Pandas_Basics as pd
from Pandas_Basics import DataFrame
import Numpy_Basics as np

cars = ["Ford", "Volvo", "BMW"]

# print(cars)
# print(pd.DataFrame(cars))


cars = [["Ford", "Red"], ["Volvo", "Blue"], ["BMW", "Green"]]

# print(cars)
# print(pd.DataFrame(cars))

# Array methods !!!(NOT usabel while it is a DataFrame)!!!
#    Method	    Description
#    append()	Adds an element at the end of the list
#    clear()	Removes all the elements from the list
#    copy()	    Returns a copy of the list
#    count()	Returns the number of elements with the specified value
#    extend()	Add the elements of a list (or any iterable), to the end of the current list
#    index()	Returns the index of the first element with the specified value
#    insert()	Adds an element at the specified position
#    pop()	    Removes the element at the specified position
#    remove()	Removes the first item with the specified value
#    reverse()	Reverses the order of the list
#    sort()	    Sorts the list


# Functions__________________________________________________________


# def my_function1():
# print("Hello from a function")

# my_function1()


# Functions (lambda)_____________________________________________________________
# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression.


x = lambda a, b: a * b
# print(x(3, 6))

x = lambda a, b, c: (a + b) * c


# print(x(5, 6, 2))

lam1 = lambda varX: varX * 2
# print(lam1(5))


nm = ['greg lee Zoon', 'bob dillon', 'andrew aaron']
#print(nm)
nm.sort(key=lambda name: name.split(" ")[-1].lower())
#print(nm)




#map

mylist = [1,2,3,4,5,6,7,8]
mylambda = lambda x: x + 1
mylist = map(mylambda, mylist)
#print(mylist)

mylist = list(mylist)
#print(mylist)

    #Simpler version
mylist = list(map(lambda x: x + 1,  [1,2,3,4,5,6,7,8]))
#print(mylist)



#FILTER

lst = [1,2,3,4]

flst = list(filter(lambda x: x > 2, lst))
#print(flst)


slst = ["", "fin", "", "max", "tim"]
slst = list(filter(None, slst))
#print(slst)


#REDUCE
# Itterates over each list item
    #step 1: val1 = f(a1, a2)
    #step 2: val2 = f(val1, a3)
    #step 3: val3 = f(val2, a4)
    #...
#return val:n

import statistics
from functools import reduce

lst = [1,2,3,4,5,6,7,8,9]

lst = reduce(lambda x, y: x*y, lst)
#print(lst)










# Functions (def)
def my_function2():
    x = "Hello from a function"
    return x


# print(my_function2())


def my_function3(x):
    return x


# print(my_function3("Hello from a function"))


def my_function3(x, y):
    z = x + y
    return z


# print(my_function3(10, 20))

def my_function4(x, y):
    return x + y


# print(my_function4(10, 20))


# def my_function5(country = "Norway"):
# print("I am from " + country)

# my_function5("Sweden")
# my_function5("India")
# my_function5()
# my_function5("Brazil")


# def my_function6(country = "Norway"):
# print("I am from " + country)

# my_function6(country = "Sweden")
# my_function6(country = "India")
# my_function6()
# my_function6(country ="Brazil")







# Recursion

def fact(n):
    if n == 1:
        return n
    else:
        return n * fact(n - 1)
#print(fact(4))


def fact2(n, g, x):
    if n == 1:
        lst1.append(1)
        return n
    else:
        lst1.append(n)
        stat = 1
        for z in lst1:
            stat = z * stat
        lst2.append(stat)
        return n * fact2(n - 1, g, x)

lst1 = []
lst2 = []
lst2.append(0)
#print(fact2(12, 1, 4))

lst1.reverse()
lst1.append(1)
import pandas as pd

lst = zip(lst1, lst2)
lst = pd.DataFrame(lst)
lst.columns=['n','n!']
import numpy as np
lst.index = np.arange(1, len(lst)+1)
#print('')
#print(lst['n!'])





def fib(x):
    if x == 0 or x == 1:
        return 1
    else:
        return fib(x-1) + fib(x-2)

#print(fib(6))



def fib_dict(n, d):
    if n in d:
        return d[n]
    else:
        ans = fib_dict(n-1, d) + fib_dict(n-2, d)
        d[n] = ans
        return ans

d = {1:1, 2:2}
#print(fib_dict(30,d))






# Class_____________________________________________________________

class myFunctions:
    def function1():
        return "This is function 1"

    def function2():
        return "This is function 2"


# print(myFunctions.function1())
# print(myFunctions.function2())


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


p1 = Person("John", 36)


# print(p1.name)
# print(p1.age)


class Car:
    def __init__(self, Rego, Owner):
        self.Rego = Rego
        self.owner = Owner

    def car_full_name(Rego, Owner):
        myStr = Rego + " " + Owner
        return myStr


# print(Car.car_full_name("202-107", "Kristopher"))


class Help_text:
    """
    This is where the help text goes fo my Class
    Second Line
    """

    def __init__(self, car):
        self.car = car

    def car2(self):
        """
        This is where the help text goes fo my Function
        Second Line
        """
        return "String"

# help(Help_text)
# help(Help_text.car2)
