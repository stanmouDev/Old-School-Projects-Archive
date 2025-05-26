hello = '''"just like knowledge, you cant take self-discipline for granted. " \
        "unfortunately, being a self-disciplined person isn't a "one and done" kind of thing.
         Once you have learned how to live that way, you can still lose it if you don't consistently strengthen it 
         by setting new challenges and rejecting instant gratification in favor of bigger future rewards" '''
print(len(hello))

print(hello[4:20])


def call_me(firstname):
    print(firstname + ":", "Micheal")


call_me("Ben")
call_me("Mike")
call_me("john")
call_me("Macbeth")
call_me("stanley")

# first 10 multiple of 6

number = int(input("enter number: "))

print("the multiples are: ")
for i in range(1, 10):
    print(number * i, end=" ")


def row(s, n):
    return s * n


print(row("hello world! ", 5))


def mult(x, y):
    return x * y


num1 = 90
num2 = 89

print(mult(num1, num2))

list1 = [5, 7, 9, 4]
list2 = [3, 9, 8, 7]
multiply = []
for number1, number2 in zip(list1, list2):
    multiply.append(number1 * number2)

print(multiply)

import math

list1 = [20, 10, 15, 16]
list2 = [14, 12, 16, 11]
p1 = math.prod(list1)
p2 = math.prod(list2)
print("the product of list1 is: ", p1)
print("the product of list2 is: ", p2)


def multiplylist(my_list):
    r = 1
    for a in my_list:
        r = r * a
    return r


list1 = [3, 5, 6]
list2 = [7, 9, 8]
print(multiplylist(list1))
print(multiplylist(list2))

# first 10 multiple of 8

number = int(input("enter the number"))

print("the multiple are: ")
for i in range(1, 10):
    print(number * i, end=" ")

# first 20 multiple of 4

number = int(input("enter the number: "))

for i in range(1, 20):
    print(number * i, end=" ")

# first 5 multiple of 2

number = int(input("enter the number: "))

for i in range(1, 5):
    print(number * i, end=" ")


def mult(x, y):
    return x * y


num1 = 5
num2 = 6

print(mult(num1, num2))

number = 171 * 5
print("the product is ", number)

number = 5 * 8
print(number)

num1 = complex(3, 4)
num2 = complex(2, 5)
result = num1 * num2
print(result)

# multiplying complex numbers

num1 = complex(3, 4)
num2 = complex(5, 6)
result = num1 * num2
print(result)


def row(s, n):
    return s * n


print(row("hello world!", 5))

num1 = complex(4, 6)
num2 = complex(8, 3)
num3 = complex(2, 9)
result = num1 * num2 + num3
print(result)

number = int(input("enter the number"))
print("the product is ", number)
number = 8 * 9
print(number)

