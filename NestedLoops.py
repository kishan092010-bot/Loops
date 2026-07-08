# Nested Loops - It means a loop inside another loop

# Syntax:
# for outer in range(3):
#     for inner in range(5):
#         print(outer, inner)
# i = 1
# 
# while loop inside while loop 

# Assignment 1: Program using Nested Loops
i = 1
while i <= 3:
    j = 1
    while j <= 5:
        print(i,j)
        j = j + 1
    i = i + 1

# Assignment 2: 

for i in range(3):

    for j in range(5):
        print("*", end = " ")
    print()

# Assignment 3:

word = input("Please enter your word:")
char = input("Please enter your own character:")
i = 0
count = 0

while i < len(word):
    if word[i] == char:
        count = count + 1
    i = i + 1
print("The total number of times", char, "has occured = ", count)