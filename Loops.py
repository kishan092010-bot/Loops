# 1. For Loop

# A for loop is used to repeat a block of code a fixed number of times or to go through every item in a sequence like a string, list, or range.

# Real-Life Example:

# Imagine you have 10 books on a shelf. You pick each book one by one to check its title. You know exactly how many books there are. This is like a for loop.

# 2. While Loop

# A while loop repeats the code as long as a condition is True.

# Real-Life Example:

# You keep washing dishes while there are dirty dishes.

# 3. Nested Loop

# A nested loop is a loop inside another loop.

# Real-Life Example:

# For every student in the class, check every subject.

# Student 1

# Math

# Science

# Student 2

# Math

# Science

#Syntax of a For Loop

# for variable in sequence:

# statement

# Let's Understand Each Part

#1. for

# Meaning

# Starts a loop.

# It tells Python,

# "Repeat this block of code."

#2. i

# This is called the loop variable.

# It stores one value at a time.

# First → 0

# Second → 1

# Third → 2

# Fourth → 3

# Fifth → 4

# Think of it as a box that changes every time the loop runs.

#3. in

# Means

# Take values from...

# 4.range(5)

# Creates numbers

# 0

# 1

# 2

# 3

# 4

# Notice

# It stops before 5.

# :

# 5.Colon means

# "The loop body starts here."


# Assignment 1: To find the sum of numbers

for i in range(1,6):
    print(i)

n = int(input("Enter a number whose sum you want to find: "))
sum = 0

for i in range(1,n):
    sum = sum + i
    print(sum)


# Assignment 2: Reverse a String

n = input("Enter a name: ")
print(n)
string2 = ""
for i in n: 
    string2 = i + string2
    print(string2)
print("Hello"+" "+"world")

# Assignment 3

n = int(input("Enter the value of n:"))
for i in range(n,0,-1):
    print(i)
print("***********************************************************")
for i in range(0,n,2):
    print(i)


# While Loops - It keeps running as long as the condition is true

# Syntax - While condition:
              # Statement


# Assignment 1

n = int(input("Enter the value of a number: "))
sum = 0
i = 1

while i <= n:
    print("The value of i is:", i)
    print("Before sum value:", sum)
    sum = sum + i
    print("After sum value:", sum)
    i = i + 1

print("Sum is equal to:", sum)

# Assignment 2: Armstrong Number

 # It's a number where the sum of the cubes of its digits equals the original number.

    # E.g:
    # 153 = 1**3 + 5**3 + 3**3 = 1 + 125 + 27 = 153 again

num = int(input("Enter a number: "))
sum = 0
temp = num
print(num)

while temp > 0:
    digit = temp % 10
    sum += digit ** 3
    temp //= 10 

if num == sum:
    print(num, "is an armstrong number.")

else:
    print(num, "is not an armstrong number.")