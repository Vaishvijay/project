#1.program to print the following string in a specific format
"""
print("Twinkle, twinkle, little star,\n\t\tHow I wonder what you are!\n\t\t\t\tUp above the world so high,\n\t\t\t\tLike a diamond in the sky.\nTwinkle, twinkle, little star,\n\t\tHow I wonder what you are! ")


#2.program to get the Python version you are using.

import sys
print(sys.version)
#print(sys.version_info)
#print(sys.api_version)



#3. program to display the current date and time.

from datetime import datetime

now = datetime.now()
print("Current date and time: \n")
print(now.strftime("%Y-%m-%d %H:%M:%S "))



#4. program which accepts the radius of a circle from the user and compute the area.
from math import pi
r =  float(input("r="))
print("Area = " + str(pi*r*r))


#5. program which accepts the user's first and last name and print them in reverse order with a space between them.

f_name = input("Enter first name:")
l_name = input("Enter last name:")
print(l_name + " " +f_name )

name = input("Enter first and last name:")

rev = name[::-1]
print(rev)



#6. program which accepts a sequence of comma-separated numbers from user and generate a list and a tuple with those numbers

input1 = input("Sample input : ")
print(input1.split(",")) #split fn returns a list
print(tuple(input1.split(",")))



#7. program to accept a filename from the user and print the extension of that.

filename = input("Enter a filename: ")
ext = filename.split(".")
print("Extension is " + str(ext[-1]))


#8. program to display the first and last colors from the following list.

color_list = ["Red","Green","White" ,"Black"]
print(color_list[0])
print(color_list[-1])


#9. program to display the examination schedule.

exam_st_date = (13,12,2020)
print("Examination date is:  %i/%i/%i"%exam_st_date)


#10. program that accepts an integer (n) and computes the value of n+nn+nnn

num = int(input("Enter a number: "))
n1 = int("%s" %num)
n2 = int("%s%s" % (num,num))
n3 = int("%s%s%s" % (num,num,num))

print("Result is: "+ str(n1+n2+n3))



#print(pow.__doc__)

from datetime import date
f_date = date(2014, 7, 2)
l_date = date(2014, 7, 11)
delt = l_date - f_date
print(delt.days)


#11. program to get the difference between a given number and 17, if the number is greater than 17 return double the absolute difference

num = int(input("Enter a number: "))
if num > 17:
    print((2*(num-17)))
else:
    print(17 - num)

#12. program to calculate the sum of three given numbers, if the values are equal then return three times of their sum.

#n1 = int(input("Enter first number: "))
#n2 = int(input("Enter second number: "))
#n3 = int(input("Enter third number: "))

def add(n1,n2,n3):
    sum = n1+n2+n3
    if(n1==n2 and n2==n3):
        return n1*sum
    else:
        return sum
print(add(1,2,3))
print(add(3,3,3))



#13. program to get a new string from a given string where "Is" has been added to the front. If the given string already begins with "Is" then return the string unchanged.

def string(name):
    if len(name)>2 and name[:2] == "Is":
        return name
    else:
        return "Is" + name
print(string("Ismale"))
print(string("hi"))



#14. program to find whether a given number (accept from the user) is even or odd, print out an appropriate message to the user.

num = int(input("enter a number: "))
if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")


#15. program to count the number 4 in a given list.

def arr(number):
    count = 0
    for num in number:
        if num == 4:
            count = count + 1

    return count

print(arr([1,3,5,6]))


#16. program to test whether a passed letter is a vowel or not.

letter = input("Input a letter: ")
if letter.lower() in "aeiou":
    print("VOwel")
else:
    print("no")


#17. program to check whether a specified value is contained in a group of values.

group = input("Enter values: ")
list = group.split(",")
print(list)
search = input("Enter the value to be searched: ")
if search in list:
    print("found")
else:
    print("not found")


#18. program to create a histogram from a given list of integers

def histogram(values):
    for value in values:
        op = ""
        times = value
        while (times > 0):
            op = op + "#"
            times = times-1
        print(op)
histogram([2,3,5,6])



#19. program to concatenate all elements in a list into a string and return it.

def concate(ele):
    op = ""
    for values in ele:
        op = op + str(values)
    return op
print(concate([1,5,12,2]))


#20. program to print all even numbers from a given numbers list in the same order and stop the printing if any numbers that come after 237 in the sequence.

def even(list):
    for nums in list:
        if nums != 237:
            if nums % 2 == 0:
                print(nums)

        else:
            print(nums)
            break;
even([386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,
    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,
    815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717,
    958,743, 527])


#21. program to print out a set containing all the colors from color_list_1 which are not present in color_list_2.

color_1 = set(["White", "Black", "Red"])
color_2 = set(["Red", "Green"])
print("First list: " +str(color_1))
print("Second list: "+str(color_2))
#DIFFERENCE OF SETS: A-B OR A.diferrence(B)
print("Difference is: "+str(color_1 - color_2))
#print("Difference is: "+ str(color_1.difference(color_2)))

#22. program that will accept the base and height of a triangle and compute the area.

def area(base,height):
    return (base*height) * 0.5
print(area(20,40))


#23. program to compute the greatest common divisor (GCD) of two positive integers.

def gcd(a, b):
    if (b == 0):
        return a
    else:
        return gcd(b, a % b)
print("The gcd of 60 and 48 is : ")
print(gcd(60, 48))


from math import *
n1 = int(input("Enter a number: "))
n2 = int(input("Enter a number: "))
print(gcd(n1, n2))


#24. program to sum of three given integers. However, if two values are equal sum will be zero.

def sum(a, b, c):
    if (a == b) or (b == c) or (c == a):
        return 0
    else:
        return a + b +c
print(sum(1,2,1))
print(sum(1,3,2))



#25. program to sum of two given integers. However, if the sum is between 15 to 20 it will return 20.

def sum(a, b):
    c = a + b
    if c in range(15, 20):
        return 20
    else:
        return c
print(sum(20, 50))
print(sum(2, 3))
print(sum(10, 5))


#26. program that will return true if the two given integer values are equal or their sum or difference is 5.

def sum_diff(a,b):
    sum = a + b
    diff = a - b
    if(a == b) or (sum == 5) or (diff == 5):
        return True
    else:
        return False
print(sum_diff(1,1))
print(sum_diff(3, 2))
print(sum_diff(10, 5))
print(sum_diff(7, 8))


#27. program to solve (x + y) * (x + y).

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
res = ((x+y) ** 2)
print(res)


#28. program to compute the future value of a specified principal amount, rate of interest, and a number of years.

amt = float(input("Enter amount: "))
int = float(input("Enter interest: "))
yrs = float(input("Enter years: "))
res = (amt*int*yrs)/100
print(res)


#29. program to find the sum of the first n positive integers.

n = int(input("Enter number:"))
sum = (n* (n+1)) /2
print(sum)


#30.  program to convert height (in feet and inches) to centimeters.

print("Enter your height: ")
h_ft = float(input("Feet: "))
h_in = float(input("Inches: "))
h_in = h_in + (h_ft * 12)
h_cm = h_in *2.5
print("your height is %f cm: "% h_cm)


#31. program to calculate the hypotenuse of a right angled triangle.
from math import *
opp = int(input("Enter opposite side of triangle: "))
adj = int(input("Enter opposite side of triangle: "))
hyp = sqrt(opp**2 + adj**2)
print(hyp)


#32.  program to sort three integers without using conditional statements and loops.

x = int(input("Input first number: "))
y = int(input("Input second number: "))
z = int(input("Input third number: "))

min = min(x,y,z)
max = max(x,y,z)
sum = x + y + z
mid = sum - max - min
print(min,mid,max)

#33. function to create and print a list where the values are square of numbers between 1 and 30 (both included).

def square():
    l = list()
    for i in range(1,31):
        l.append(i**2)
    print(l)
square()

"""