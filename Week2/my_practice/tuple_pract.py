# creating a tuple


# A tuple is created by placing all the items (elements) inside parentheses (), separated by commas. The parentheses are optional, however, it is a good practice to use them.

my_tuple = 1,2,3,4
print(my_tuple)
print(type(my_tuple))

var1 = "hello"
print("var1:", type(var1))

var2 = "hello",
print("var2:", type(var2))

var3 = ("hello")
print("var3:", type(var3))

var4 = ("hello",)
print("var4:",type(var4))


# Python Tuple Methods

# Only Two methods are available. i.e .count() & .index()

# Unpacking a tuple

front_end = ("html","css","javascript")
content,styling,interactivity = front_end 

print(content)