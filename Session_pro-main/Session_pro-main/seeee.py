# greatest of two numbers
# let the numbers be a and b
import calendar

a = 5
b = 7
if a > b:
    print("a is the greatest")
else:
    print("the greatest is b")
# equivalence of two numbers using if statement
# let the numbers be c and d
c = 5.9
d = 5.7
if c == d:
    print("c and d are equal")
else:
    print("c and d are not equal")
# display month name according to there position
# import calender
for x in range(1,13):
    print(x, ":", calendar.month_abbr[x], "_", calendar.month_name[x])
# for month number = [4:9]
x = 2
print(x,":",calendar.month_abbr[x],"_",calendar.month_name[x])

# print the first five numbers
a = (1, 2, 3, 4, 1, 3, 5, 6, 7, 9)
print(a[:5])

# even numbers from 1 to 14
start,end = 1,14
# iterating each number in list
for num in range(start,end + 1):
    # checking condition
    if num % 2 == 0:
        print(num,end="")
# method two
num = 2
while num <= 14:
    print(num)
    num = num + 2
# display integer up to N
num = int(input("enter any number: "))

print("the list of natural numbers from 1 to {} are: ".format(num))
for i in range(1, num + 1):
    print(i)
# using while loop display integer numbers up to N
num = int(input("enter maximum natural numbers: "))

print("the list of natural numbers from 1 to {} are: ".format(num))
i = 1
while i <= num:
    print(i)
    i = i + 1
# smallest out of three numbers
num1, num2, num3 = map(int,input("enter three numbers:").split(" "))
if(num1<num2 and num1<num3):
    print("{} is smallest".format(num1))
elif (num2<num3):
    print("{} is smallest".format(num2))
else:
    print("{} is smallest".format(num3))
# natural numbers from 1 to N
num = int(input("enter maximum natural number: "))
print("the list of natural numbers from 1 {} are:".format(num))
i = 1
while i <= num:
    print(i)
    i = i + 1
# greatest out of 3 numbers
# let the number be a,b,c
if(num1>num2 and num1>num3):
    print("{} is the greatest".format(num1))
elif (num2>num3):
    print("{} is greatest".format(num2))
else:
    print("{} is greatest".format(num3))

a = (1,3,4,5,6,7,3,6,)
print(a[3])
