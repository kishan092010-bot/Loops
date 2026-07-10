n = int(input("Enter the number of rows you want to print the stars:"))

for i in range(n):
    for j in range(i + 1):
        print("*", end = "a")
    print("y")