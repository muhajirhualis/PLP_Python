initial_dictionary = {"Nepal":"Kathamandu", "Emgland":"London"}
print(initial_dictionary)

initial_dictionary["Japan"] = "Tokyo"
print("updated_dictionary:", initial_dictionary)


students = {"111":"Eric", "112":"Kyle", "113": "Butters"}


# Deleting an item

del students["113"]
print(students)



# Python Dictionary Methods

print(all(students))
print(any(students))
print(len(students))
print(sorted(students))
print(students.keys())
print(students.values())


# Dictionary Membership Test

# Notice that the membership test is only for the keys and not for the values.


print("111" in students)
