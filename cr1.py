# 1. User's name and age
name = input("Enter your name: ")
age = int(input("Enter your age: "))
print(name)
print(age)

# 2. Sum of two numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("Sum:", a + b)

# 3. Count words in a file
with open("file.txt", "r") as f:
    words = f.read().split()
    print("Number of words:", len(words))

# 4. Write sentence to file in reverse order
sentence = input("Enter a sentence: ")
with open("output.txt", "w") as f:
    f.write(sentence[::-1])

# 5. Read CSV and convert to dictionary
import csv
with open("data.csv", newline="") as f:
    reader = csv.DictReader(f)
    data = [row for row in reader]
print(data)

# 6. Monitor log file for keyword
keyword = "ERROR"
with open("log.txt") as f:
    for line in f:
        if keyword in line:
            print("Alert:", line)