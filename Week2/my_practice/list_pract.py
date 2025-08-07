list = [1,2,2,3,4,5]

#Adding Item to a list

list.append(6)
print(list)

list.insert(len(list),7)
print(list)

list.extend([8,9,10])
print(list)



#Removing Items from a List

list.pop()
print(list)

list.pop(8)
print(list)

del list[7]
print(list)

list.remove(2) #removes 1st occurence of value 
print(list)


# Slicing an element from a list

# Note: When we slice lists, the start index is inclusive but the end index is exclusive.


languages = ["python","swift", "C++"]
my_list = ["p","r","o","g","r","a","m","m","i","n","g"]
print(my_list[2:5])

print(languages[-3])


print(my_list.index("g"))
print(my_list.count("g"))



# sorting a list

# 👉 .sort() modifies the list in place and returns None — not the sorted list.
# ✅ Use sorted() when you want to keep the original list. 


list = [1,2,2,3,4,5]

list.sort()
print(list)

sorted_list = sorted(list)
print("sorted_list:", sorted_list)


# reversing a list

list.reverse()
print(list)

reversed_list = list[::-1]
print("reversed_list :",reversed_list)


# copy a list

print(list.copy())


# Python List Comprehension

# A list comprehension consists of an expression followed by the for statement inside square brackets.

numbers = [number*number for number in range(1,6)]
print(numbers)