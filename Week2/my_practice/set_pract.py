# A set can have any number of elements and they may be of different types (integer, float, tuple, string etc.). But a set cannot have mutable elements like lists, sets or dictionaries as its elements.


student_id = {111,112,113,114,115}
vowel_letter = {"a","e","u","i","o"}
mixed_set = {"hello", 1143, True, 12.87}

print(student_id)
print(vowel_letter)
print(mixed_set)


# Empty Set

empty_set = set()
empty_dict = {}

print(type(empty_set))
print(type(empty_dict))


# Adding Item to a set

student_id.add(116)
print(student_id)

# Updatting elements in a set

consonant_letter = ("b","v","c","d")
vowel_letter.update(consonant_letter)

print(vowel_letter)

# Removing an elements
student_id = {111,112,113,114,115}

student_id.discard(111)
print(student_id)


# Built-in Functions with Set


print(sum(student_id))

# The enumerate() function 

# -> it adds a counter to an iterable and returns it as an enumerate object (which you can loop over).

# syntax:
# for index, value in enumerate(iterable):
#     print(index, value)

# Example:

fruits = {"apple", "banana", "cherry"}

for index, fruit in enumerate(fruits):
    print(index, fruit)


# Python Set Operations

A = {1,2,3,5}
B = {0,2,4}

#Union

print(A.union(B))
print(A|B)

# Intersection
print(A.intersection(B))
print(A & B)

# Difference
print(A.difference(B))
print( A-B)

#Symmetric Difference
print(A.symmetric_difference(B))
print(A^B)