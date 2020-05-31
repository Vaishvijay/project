from math import *
""""
print("    /|")
print("   / |")
print("  /  |")
print(' /___|')
phrase = "Vaish Manie"
print("Vaish Manie")
print("Vaish\nManie")
print("Vaish\"Manie")
print(phrase + " are cute")
print(phrase.upper())
print(phrase.lower())
print(phrase.isupper())
print(phrase.upper().isupper())
print(len(phrase))
print(phrase[0])
print(phrase.index("M"))
print(phrase.index("aish"))
print(phrase.replace("Manie","Man"))


print(2)
print(-2)
print(3.4 + 4)
print(4 * (4+7))
print(10 % 3)
my_num = 5
print(my_num)
print(str(my_num) + " my faviee")
my_num1 = -5
print(abs(my_num1))
print(pow(3,2))
print(max(4,6))
print(min(4,6))
print(round(3.3))
print(round(3.7))
print(floor(3.7))
print(ceil(3.7))
print(sqrt(36))

name = input("Enter your name: ")
age = input("Enter age: ")
print("Hello " + name + "! You are " +age)

num1 = input("Enter a number: ")
num2 = input("Enter a number: ")
result = float(num1) + float(num2)

print(result)

color = input("Enter a color: ")
plural_noun = input("Enter a plural noun: ")
celeb = input("Enter a celeb name: ")

print("Roses are " + color)
print(plural_noun +" are blue")
print("I love " + celeb)

#LIST

friends = ["Manie", "Man", "Manuel", "Cless"]
print(friends)
print(friends[0])
print(friends[-1])
print(friends[1:])
print(friends[1:3])
friends[1] = "Ro"
print(friends[1])

lucky_num = [7, 5, 6, 9, 0, 1]
friends = ["Manie", "Manie","  Man", "Manuel", "Cless"]
#friends.extend(lucky_num)
friends.append("Creep")
friends.insert(1,"Kelly")
friends.remove("Kelly")
#friends.clear()
friends.pop()
print(friends)
print(friends.index("Cless"))
print(friends.count("Manie"))
friends.sort()
print(friends)
lucky_num.sort()
print(lucky_num)
lucky_num.reverse()
print(lucky_num)

friends2 = friends.copy()
print(friends2)

#TUPLES

#coordinates = (4,5)
coordinates = [(4,5), (6,7), (80,34)]
coordinates[0] = 10
print(coordinates[0])

#FUNCTIONS

#define a function
def say_hi():
    print("Hello User")
#call a function
say_hi()

def say_hi(name, age):
    print("hello " +name + "! You are " + str(age))
say_hi("Vaish", 22)
say_hi("Manie", 24)

#RETURN STATEMENT

def cube(num):
    return num*num*num

result = cube(3)
print(result)

#IF

is_male = True
if is_male:
    print("You are a male")
else:
    print("You are a female")

is_male = True
is_tall = False
if is_male and is_tall:
    print("You are a tall male")
else:
    print("You are either not a male or tall or both")


is_male = True
is_tall = False
if is_male or is_tall:
    print("You are either a male or tall or both")
else:
    print("You are not both nor male nor tall")



is_male = True
is_tall = False
if is_male and is_tall:
    print("You are a tall male")
elif is_male and not(is_tall):
    print("You are a short male")
elif not(is_male) and is_tall:
    print("You are a not a male but tall")
else:
    print("You are not a male nor tall")



def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >=num1 and num2 >= num3:
        return num2
    else:
        return num3

print(max_num(54,34,67))

num1 = float(input("Enter first number: "))
op = input("Enter operator: ")
num2 = float(input("Enter second number: "))

if op == '+':
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "*":
    print(num1 * num2)
elif op == "/":
    print(num1 / num2)
else:
    print("Invalid")


#DICTIONARY

monthConversions = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December"
}

print(monthConversions["Dec"])
print(monthConversions.get("Nov"))
print(monthConversions.get("Luv", "Not valid"))


#WHILE LOOP

i = 1
while i <= 10:
    print(i)
    i += 1


#GUESSING GAME

secret_word = "Giraffe"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False

while guess != secret_word and not(out_of_guesses):
    if guess_count < guess_limit:
        guess = input("Enter guess: ")
        guess_count += 1
    else:
        out_of_guesses = True

if out_of_guesses:
    print("you are out of guesses!")
else:
     print("You win!")


#FOR LOOP

for letter in "Vaishali":
    print(letter)

friends = ["Cless", "Man", "Ro"]
for friend in friends:
    print(friend)

for index in range(10):
    print(index)

for index in range(3,10):
    print(index)


friends = ["Cless", "Man", "Ro"]
for index in range(len(friends)):
    print(friends[index])


if 402 % 2 == 0:
    print(402)

#EXPONENT FUNCTION

def exp(base, pow):
    result = 1
    for index in range(pow):
        result = result * base
    return result
print(exp(2, 3))


#2D LISTS AND NESTED LOOPS

number_gird = [
    [1,2,3],
    [4,5,6],
    [7,8,9,],
    [0]
]

#print(number_gird[0][0])

for row in number_gird:
    for col in row:
        print(col)


#TRANSLATOR

def translator(phrase):
    translation = ""
    for letter in phrase:
        if letter.lower() in "aeiou":
            if letter.upper() in phrase:
                translation = translation + "G"
            else:
                translation = translation + "g"
        else:
            translation = translation + letter
    return translation

print (translator(input("Enter a phrase")))

#TRY/EXCEPT

try:
    value = 10/ 0
    num = int(input("Enter a number:"))
    print(num)
except ZeroDivisionError as err:
    print(err)
except ValueError:
    print("Invalid input")



#READING FILES

file = open("emp.txt","r")
#r is mode ie read w write a append r+ read and write

#gives a boolean result if file readable or not
print(file.readable())
#reads the file
print(file.read())
#read a line at a time
print(file.readline())
#takes each line and puts inside an array
print(file.readlines())
#if we want to print one specific line
print(file.readlines()[1])
#to print each line in the file
for employee in file.readlines()
    print(employee)
file.close()

#WRITING TO FILES

file = open("emp.txt","a")
#if w is used then everything in emp.txt will be replaced
#abcd will be added to emp.txt at the end of the file as mode is a
file.write("abcd")
file.close()



#MODULES AND PIP

#CLASSES AND OBJECTS

#in Student file define a class
class Student:
    def __init__(self, name, sun, id):
        self.name = name
        self. sun = sun
        self.id =id

#in app.py import class file

#from Student import Student
#stud1 is object
stud1 = Student("Vaish","Math","42")

print(stud1.name)


# MULTIPLE CHOICE QUIZ

#INHERITANCE

class B(A):
#B is a class inheriting from A
#we can override a function by defining the same function in B class

"""
from Mcq import Mcq

ques = [ "1.Which colour is apple?\n(a) Red\n (b) Green (c) Yellow",
             "2.Which colour is banana?\n(a) Red\n (b) Green (c) Yellow",
             "3.Which colour is parrot?\n(a) Red\n (b) Green (c) Yellow",
]
questions =[
    Mcq(ques[0],"a"),
    Mcq(ques[1],"c"),
    Mcq(ques[2],"b")
]
def run(questions):
    score=0
    for q in questions:
        answer = input(q.ques_prompt)
        if answer == q.ans:
            score +=1
    print(str(score) + "/" +str(len(questions)))
run(questions)

