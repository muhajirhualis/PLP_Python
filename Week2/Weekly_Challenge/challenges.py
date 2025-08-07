# Tasks:

#1. Write a program that accepts user input to create a list of integers. Then, compute the sum of all the integers in the list.

"""

list_int = []

for i in range (1,5):
  
  user_int = int(input("Enter an Integer:").strip())
  list_int.append(user_int)

sum_int = sum(list_int)

print("list of integers created :", list_int)
print("sum of all integers in the list =", sum_int)

"""


#2. Create a tuple containing the names of five of your favorite books. Then, use a for loop to print each book name on a separate line.

"""
fav_books = ("Quran","Bukhari","Muslim","Nesai","Ibnu Majeh")

for book in fav_books:
  print(f"{book} \n")

"""

#3. Write a program that uses a dictionary to store information about a person, such as their name, age, and favorite color. Ask the user for input and store the information in the dictionary. Then, print the dictionary to the console.

"""
name = input("Enter your Name:")
age = int(input("Enter your age:").strip())
color = input("Enter Your Favorite Color:")


person = {"name": name, 
          "age":age, 
          "favorite_color": color
          }

print(person)
"""


#4.  Write a program that accepts user input to create two sets of integers. Then, create a new set that contains only the elements that are common to both sets.

"""
set1 = set()
set2 = set()

for i in range(1,3):
  input1 = input("Enter an integer for set1:")
  set1.add(input1)
  input2 = input("Enter an integer for set2:")
  set2.add(input2)

new_set =set1.intersection(set2)
print(new_set)

"""

#5. Create a program that stores a list of words. Then, use list comprehension to create a new list that contains only the words that have an odd number of characters.

"""
sentence = "There are many variations of passages of Lorem Ipsum available, but the majority have suffered alteration in some form, by injected humour, or randomised words which don't look even slightly believable."

words = sentence.split()
print(words)

new_words = [word for word in words if len(word) % 2 != 0 ]
print(new_words)


"""