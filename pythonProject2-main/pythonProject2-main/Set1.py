print(type(123))
# greatest of two numbers
a = 4
b = 40
if a > b:
    print("a is the greatest")
else:
    print("the greatest is b")
# string arrays
a = "hello, world!"
print(a[3])
# loop
x = "banana:"
print(x[2:4])
a = (1, 2, 3, 4, 5, 6, 7, 8, 9)
print(a[2:4])
a = "hello, world!"
print(len(a))
# Check if "LONDON" is present in the following text:
txt = "Is LONDON a Capital of Britain?"
print("LONDON" in txt)
if "LONDON" in txt:
    print("Yes, 'LONDON' is present.")
# Check if "Scotland" is NOT present in the following text:
txt = "Is London a Capital of Britain?"
print("Scotland" not in txt)
# print only if "Scotland" is NOT present:
txt = "Is London a capital of Britain"
if "Scotland" not in txt:
    print("No, 'Scotland' is NOT present.")
# Get the characters from the start to position 5 (not included):
b = "Hello, Moto!"
print(b[:8])
# Get the characters from position 2, and all the way to the end:(slicing)
b = "Hello, Moto!"
print(b[2:])
# Get the characters:
# From: "o" in "Moto!" (position -4) To, but not included: "o" in "Moto!" (position -2):
b = "Hello, Moto!"
print(b[-5:-2])
a = 6800
b = 31.3
if b > a:
    print("b is greater than a")
else:
    print("b is not greater than a")
a = 33
b = 33
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")
a = 33
b = 200
if b > a:
    print("b is greater than a")
# preceding conditions.
a = 33
b = 200
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")
else:
    print("a is greater than b")
a = (1, 2, 3, 4, 5, 6,)
print(a[:4])
a = input("what is your level of confidence? low")
print("my level of confidence is:" + "High")
#  WRITE A PSEUDOCODE TO FIND THE AREA OF RECTANGLE.
L: float = float(input('Enter the length of a Rectangle: 30'))
B: float = float(input('Enter the breadth of a Rectangle: 10'))
Area: float = L * B
print(("Area of a Rectangle is: %.2f" % Area))