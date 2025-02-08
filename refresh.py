print ()
print("Bach")
king = "King Bach"
print(king)
print()
Kingslist = ["Bugatti", "Toyota", "LC600", "Subaru"]
print (Kingslist)
'''
To add an item to the end of the list, we use the append() method:
To add an item at the specific index, use the insert() method:
To remove an item, use the remove() method: - del() keyword removes the specified index
Clear () method empties the list
'''
Kingslist = ["Bugatti", "Toyota", "LC600", "Subaru"]
Kingslist.append("Volks Wagen")
print(Kingslist)
Kingslist.insert(2, "Mercedes-Benz")
print(Kingslist)
Kingslist.remove("LC600")
print(Kingslist)
print(len(Kingslist))
print(len(king))
print()
print("Types of numbers")
x=1
y=2.5
z=5j

print(type(x))
print(type(y))
print(type(z))
print()


'''
format() method is used to combine strings and numbers, eg
'''
King = 23
txt = "King Bach has {} million."
print(txt.format(King))
print()
print("Boolean")
'''
Boolean
when you run a condition in an if statement, Python returns True or Fale.

'''
print(23 < 22)
print(22==22)
print(22>19)
'''
COPY - copy()
'''
print()
print("Copying")
Kingslist = ["Bugatti", "Toyota", "LC600", "Subaru"]
mylist=Kingslist.copy()
print(mylist)
print()
'''
               ARRAYS
*list []      Ordered and change-able
*tuple ()     Ordered and unchangble
*sets {}      unordered and un indexed, items can be added,
              items can be accessed using 'for' loop, can be updated using 'update()'
              'remove ()' can be used to remove an item in the set
              'del' keyword will delete the set compeletely 
*dictionary {} unordered, changeable and indexed
'''
print("Arrays")
Bachslist=["Oraimo", "Bosse", "LG", "Samsung", "Oppo", "Sony"]
print(Bachslist)
Bachslist.remove ("Bosse")
print(Bachslist)
Bachslist.insert(2, "JBL")
print(Bachslist)
Bachsdictionary = {
    "brand": "Ford",
    "model":"Mustang",
    "year": 1964
    }
print(Bachsdictionary)
j=Bachsdictionary.get("brand")
print(j)
print()
'''
we can change values by referring to the keyword, eg "year"
'''
Bachsdictionary["year"]=2023
print(Bachsdictionary)
x = Bachsdictionary["model"]
'''
you can loop throgh a dictionary using a 'for' loop
'''
for x in Bachsdictionary:
    print(Bachsdictionary[x])
if "model" in Bachsdictionary:
  print("Yes, 'model' is one of the keys in Bach's dictionary")
'''
an item is added by using a new index key and assigning value to it
'''
print()
Bachsdictionary["color"] = "Black"
print (Bachsdictionary)
# to diplay in an oderly way..
for x, y in Bachsdictionary.items():
    print(x, y)
print()    
# we can make a copy using the 'dict()' method
mydict = dict(Bachsdictionary)
print(mydict)
print()
a=60
b=40
if b>a:
    print("b is greater")
elif a==b:
 print("a is equal to b")
else:
    print("a is greater than b")
print()
# AND logical operator is used to combine conditional statements
# if...else statements
c=100
if a>b and c>a:
    print("Both conditions are true")

if a>10 :
     print("above ten")
     if a>20:
         print("above 20")
     else:
         print("not above 100")
print()         
'''    
# while loops
can execute a statement as long as a condition is true
'''
i=1
while i<6:
    print(i)
    i += 1
# with the 'else' ststement, we can run a condition when the block is false e.g
else :
    print("i is greater than 6")
print()    
'''
# for loops
used to create an iterating list, ie ordered e.g
'''
Bachfruits=["mangoes", "apples", "bananas"]
for x in Bachfruits:
    print(x)
for x in "bananas":
    print (x)
# with the 'break' statement, we can stop the loop before it has looped through all items    
for x in Bachfruits:
    print(x)
    if x== "apples":
        break
# The range functiom, the range can also be specified (y)
for x in range(6):
    print(x)
for x in range (11, 16):
    print(x)
print()    
for y in range (2, 30, 3):
    print(y)
else:
    print("Not in range")
print()    
# Nested loops - loop inside a loop
adj = ["big", "black", "fast"]
cars = ["toyota", "mazda", "nissan"]
for x in adj:
    for y in cars:
        print(x, y)
print()
'''
FUNCTIONS
*A block of code which only runs when called
*You can pass data and parameters into a function
*A function can return data as a result
* created using the 'def' keyword e,g
'''
print("Start of functions")

def Bachs_function():
    print("Hello from Bach's function")
print()    

Bachs_function()
def my_function(fname):
    print(fname + " Kingbach")

my_function("Email:")
my_function("Name:")
my_function("Loyalty:")
print()
Bachs_function ()
print ()
def my_function(fname, lname):
  print(fname + "   " + lname)

my_function("King", "Bach")
print()
'''
Python Lambda
* Small anonymus function
* Can take any number of arguments but can only have one expression
Syntax
    lamdda arguments : expression
'''
x = lambda a : a + 10
print(x(5))
x = lambda a ,b : a * b
print(x(5, 6))
x = lambda a, b, c : a + b + c
print(x(5, 10, 3))
print()
def my_func(lname):
    print(lname)
    return lambda a : a * 5
mydoubler = my_func(2)
mytripler = my_func(3)
print(mydoubler(5))
print(mytripler(7))
my_func("Email")
print()

# Python uses lists as arrays to store multiple values in one single variable
'''
Python Classes and Objects
* A class is a blueprint of creating an object
* We use the keyword 'class' to create a class
'''
print("Classes and Objects")
print()
class Bachsclass:
    x = 10
    
print(Bachsclass)
BachsObject = Bachsclass()
print(BachsObject.x)
print()
'''
The _init_()Function
* Used to assign values to object properties,
   or other operations that are necessary to do when
   the ogject is being created,
'''
class cars:
    def __init__(about, name, price, age, year):
        about.name = name
        about.price = price
        about.age = age
        about.year = year

car1 = cars("Subaru", "2 million", "10 years", "2014 model")

print(car1.name)
print(car1.price)
print(car1.age)
print(car1.year)
print ()

'''
Object Methods
* functions that belong to the object
'''
class cars:
    def __init__(about, name, price, age, year):
        about.name = name
        about.price = price
        about.age = age
        about.year = year

    def myfunc(about):
         print("My car is a " + about.name)
     

car1 = cars("Subaru", "2 million", "10 years", "2014 model")
car1.myfunc()
print()
'''
# Inheritance
first, the parent class, just the way a normal cass is created
'''

class friends:
    def __init__(self, home, away):
        self.home = home
        self.away = away

    def printname(self):
        print(self.home, self.away)

myguys = friends("Sammy &", "GT")
myguys.printname()
print()
'''
# A child class is created and the function __init__ is added to it so that it
  can be able to store values. The super() function is then used to enable the
  child class inherit the properties of the first class. eg
'''
class close_friends(friends):
    def __init__(self, home, away):
        super().__init__(home, away)

x = close_friends("Giddy &", "Elvis")
x.printname()
print()
# we can add properties to the class e.g
        
class close_friends(friends):
    def __init__(self, home, away):
        super().__init__(home, away)
        self.lastseen = 2023

x = close_friends("Giddy &", "Elvis")
print(x.lastseen)
print()
'''
methods are like pre-defined instructions eg printname, functions that belong to an object
to create objects, we add another __init__() function. In this function,
we combine the different classes to form a compelete object. e.g
'''

class friends:
    def __init__(self, home, away):
        self.home = home
        self.away = away

    def printname(self):
        print(self.home, self.away)

class close_friends(friends):
    def __init__(self, home, away):
        super().__init__(home, away)
        self.lastseen = 2023

    def connection(self):
        print("I have a pair of friends,", self.home, self.away, "who knew each other in", self.lastseen)

myguys = friends("Sammy &", "GT")
myguys.printname()
x = close_friends("Giddy &", "Elvis")
x.printname()
x.connection()
print()
'''
# Iterations
an object that contains a countable number of values
in python the iterator protocol consists of the methods ;__iter__() and __next__()
we can also loop throug using a for loop to iterate through an object:
'''
myfruits = ("banana", "apple", "mangoe")

for x in myfruits:
        print(x)

print()        

class myNumbers:
    def __iter__(self):
        self.a = 1
        return self
    def __next__(self):
        if self.a <= 15:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration

myclass = myNumbers()
myiter = iter(myclass)

for x in myiter:
    print(x)
print()
# the global keyword can be used to create a global variable inside the local scope.
'''
def myfunc():
  global x
  x = 300

myfunc()

print(x)
'''
# It can alo be used to change a lobal variable inside a function
'''
x = 300

def myfunc():
  global x
  x = 200

myfunc()

print(x)        
'''
'''
# A module
A file containing a set of instructions you want to include in your application
~Different sets of code (functions) that are imported and included in the main code
~ we save a module (file) with the .py extension.
We import the module using the 'import' statement i.e 'moduleName.functionName'
'''

import mymodule        
mymodule.greeting("Bach")
print()

import mymodule
a = mymodule.person1["age"]
print(a)
print(b)
print()

'''
We can rename a module by creating an alias for it, using the 'as' keyword
eg, to create an alias for mymodule called mx

import mymodule as mx
a = mx.person1["age"]
print(a)

*Python has several built-in modules, which you can import whenever you like. eg
dir() function
'''
print ("Using dir() to to list all the function names belonging to this windows")
print()

import platform

x = dir(platform)
print(x)
print()
"""
We can choose to only import part of the parts from a module using the from keyword
eg
"""
from mymodule import person1
print(person1["country"])
print()
print("Date and Time:")
print("Module to display current date and time")

import datetime

x = datetime.datetime.now()
print(x)
print()
print ("Program to display current year and weekday")

import datetime

x = datetime.datetime.now()
print(x.year)
print(x.strftime("%A"))
print()
print("Creating Date objects:")

# To create a date, we use the 'datetime()' class constructor
# The datetime class requires three parameters to create a date : year, momth, day e.g

import datetime
x = datetime.datetime(2023, 7, 24)
print(x)
print()

"""
'strftime()' method is used to format dates to readable strings (words)
It takes a parameter like day and reads it in numbers. It has been used above to
display the day in words.
"""
print("The strftime() method")

import datetime

x = datetime.datetime(2023, 7, 24)

print(x.strftime("%B"))
print()
"""
Python JSON
Python has a built-in-package called json, which can be used to work with json data
using 'import json',method which coverts json code to python and 'json.dumps()'
method which converts python objects to json.
all code in this section start with 'import json'
"""

print ("Python JSON - Javascript object notation")
# convert from json to python

import json
x = '{"name":"John", "age":30, "city":"New York"}'
y = json.loads(x)
print(y["age"])
print()

#an example of coverting python objects to JSON strings

import json

x = {
  "name": "Bach",
  "age": 23,
  "married": False,
  "divorced": False,
  "children": ("None"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

# convert into JSON:
y = json.dumps(x, indent=4)
print(y)
print()
'''
Python RegEx or regular expression, is a sequence of characcters that
form a regular pattern.
*Can be used to check if a string contains the specified search pattern
* invoked by 'import re' which is used to initiate working with regular expressions
* In my words, it is a search button with options
'''

print ("Python RegEx")

import re
txt = "The rain in spain"
x = re.search("^The.*spain$", txt)
if(x):
    print("Yes, we have a match")
else:
    print("No match.")    

print("*The findall() Function")
# The findall() function returns a list containing all matches
import re
txt = "The rain in spain"
x = re.findall("ai", txt)#how many times is the sequence "ai" repeated in the above...
print(x)

print()
# The search() functionsearches the string for a match and - 
#  returns a Match Object if there is a match.
print("The Search() function")

import re
txt = "King Bach has a vision"
x = re.search("vision", txt)
print(x)
print()
'''
The Split() function returns a list where the sentence has been
broken down to individual words
'''
print ("The split() function")

import re
txt = "King Bach has a vision"
x = re.split("\\s", txt)
print(x)
# You can control the number of occurences by specifying the 'maxsplit' parameter:
import re
x = "King Bach has a vision"
x = re.split("\\s", txt, 1)# The parameter is specified here
print (x)
print()
'''
sub (function)
*The sub() function replaces the matches with the text of your choice
*\\s is the shortform of white space character
'''

print ("The sub() function")

#This code shows how to replace every space with a double underscore
import re
txt = "Kingbach has a vision"
x = re.sub("\\s", "__", txt)
print(x)
#You can control the number of sustitutions by specifying the count parameters:
import re
txt = "KingBach has a serious vision "
x = re.sub("\\s", "_@_", txt, 2)
print(x)
print()

'''
PIP - python installation package
* A package contains all the files you need from a module which are code libraries
  that you can include in your project

* we use 'import' to import the package into your project  
'''  

print("Python PIP")

import camelcase
c = camelcase.CamelCase()
txt = "King bach has a serious vision"
print(c.hump(txt))
print()

'''
Python Try Except
*The 'try' block,lets you test a block of code for errors
*The 'except' block lets you handle the error
*The 'finally' block lets yiu execute code, regardless of the result of
 the try and except blocks
'''
print("Python Try Except")

try:
    print(g)#Normally this would print an error because g is not defined
except:
    print("An exception error occured")

# you can use the 'else' to difine what to be executed if no errors were raised
try:
    print("King Bach says")
except:
    print("Something went wrong")
else:
    print("Nothing went wrong")
finally:
    print("The 'try, except & else' is finished")

# Raise an exception
'''
print("The raise keyword can be used to raise an exception, a type error e.t.c e.g:")
x = -1
if x < 0:
    raise Exception("Sorry, no numbers below zero")
# Remove the comment tripple marks to run this block and produce an error    
'''
print()

print("User input")
'''
User Input
* Python allows for user input using the input() method
'''
username = input("Enter username:")
print("My username is: " + username)
print()
'''
String Formating
*Allows us to format selected parts of our string 
*In other words, making canges to sentences and values in those sentences
*We then format the results using the format() method
* To control values in a text, we add place holders (curly brackets) {} in the text,
  and run the values through the format() method e.g
'''
print("String Formating")
price = 200
txt = "The price is {} dollars."
print(txt.format(price))
# You can add parameters inside the curly brackets to specify how to convert or display the value
txt = "The price is {:.2f} dollars."
print(txt.format(price))
# You can also add more place holders to print multiple values
quantity = 3
item_no = 450
price = 150
myorder = "I want {} pieces of item number {} for {:.2f} dollars."
print(myorder.format(quantity, item_no, price))
#If we want to refer to the same value more than once, we an use the index no
age = 25
name = "Bach"
txt = "His name is {1}. {1} is {0} years old."
print(txt.format(age, name))
'''
# We can also use named indexes by enering a name inside the curly brackets, but
  then you must use names when passing the parameters
'''
myorder = "I have a {carname}, it is a {model}."
print(myorder.format(carname = "Land Cruiser V8", model = "Toyota"))

'''
File Handling
*Python has functions for creating, reading, updating and deleting files
*Working with files uses the 'open()' function, which takes two parameters :
 FILENAME and MODE
* There are 4 different modes or methods for opening a file:
 1) 'r' - Opens file for reading, returns error if file does not exist
 2) 'a' - Append - Opens a file for appending, creates the file if it does not exist
 3) 'w' - Write - Opens a file for writing, creates the file if it does not exist
 4) 'x' - Create - Creates a specified file, returns an error if the file exists.
* You can specify if the file should be handled as binary or text mode
  "t" - Text - Default value, text mode
  "b" - Binary mode (e.g images)
'''
print()
print("File Handling")
#f = open("Bachsfile.txt") This would open bachsfile if it existed
'''
To open a new file, we use the 'open()' method with one of the following parameters (x,a,w)
"x" - Create - will create a file, returns error if the file exist
"a" - Append - will add item at the end of the line
"w" - Write - will overwrite any existing content
To write to an existing file, you must add a parameter to the 'open()' function:
'''
f = open("Bachs_demo_file.txt", "a")
f.write("This is the start of bachs demonstration file")
f.close()
f = open("Bachs_demo_file.txt", "r")
print(f.read())
'''
To delete a file, you must import the 'OS module' and run its 'os.remove()' function
'''
import os
if os.path.exists("demofile2.txt"):
    os.remove("demofile2.txt")
else:
    print("The file does not exist")
#To delete an entire folder, use the 'os.rmdir()' method (you can only remove empty folders)
print()

print ("MACHINE LEARNING")
'''
In machine learning, we have 3 main categories of DATA TYPES
1) Numerical - a) discrete data - limited to intergers e.g number of cars parked.
               b) Continuous data - Infinite value e.g price of an item
2) Categorical - cannot be measured against each other e.g yes/no values & a colour
3) Ordinal - categorical but can be measured up against each other e.g school grades

* By knowing the data type of your source, you will be able to know
  what technique to use when analyzing them.
* we import numpy (numerical python) & scipy (Scientific python) 
'''
print("Mean, Median and Mode")

print("Mean:")
# Prog to find the mean of the speed array

import numpy
speed = [99,86,87,88,86,103,87,94,78,77,85,86]
x = numpy.mean(speed)
print(x)
print("Median:")
x = numpy.median(speed)
print(x)
print()
'''
For mode we import 'stats' (statistics) from the 'scipy' method
'''
from scipy import stats
scores = [89,86,87,86,83,81,82,83,89,87,85,89,82,83,84,85]
x = stats.mode(scores)
print ("Mode:")
print(x)
print()
'''
Standard Deviation
* Describes how spread out the values are in a dataset.
* We use the Numpy std()
'''
print("Standard Deviation")
import numpy
speed = [83,84,81,88,89,80,85,83,87,8688,89]
x = numpy.std(speed)
print(x)
print()
'''
VARIANCE
* Standard deviation is the square root of variance.
* Standatd deviation multiblied by itself = variance
'''
print("Variance")
import numpy
speed = [83,84,81,88,89,80,85,83,87,8688,89]
x = numpy.var(speed)
print(x)
print()
print("End of 1st Refresh")
