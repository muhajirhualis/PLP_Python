def introduce(name, age):
    return f"My name is {name}, and I'm {age} years old."

print(introduce(age=25, name="Bob"))  # Output: My name is Bob, and I'm 25 years old.


# Anonymous Functions: Lambda

# Lambda function for adding two numbers

add = lambda x,y : x + y  
print(add(2,5))


def subtract(x,y):
  return x - y
print(subtract(2,5))


numbers = [1, 2, 3, 4]
sqr = list(map(( lambda x: x**2),numbers))
print(sqr)


# recursive Function

def factorial(n):
  if n == 1:
    return 1
  else:
    return n * factorial(n-1)
  
  
print(factorial(5))