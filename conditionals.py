# 1. 
n = 5
print("Even" if n%2==0 else "Odd")

# 2.
a,b,c = 10,20,5
if a>=b and a>=c: print(a)
elif b>=c: print(b)
else: print(c)

# 3.
age = 15
if age < 13: print("Child")
elif age <= 19: print("Teen")
else: print("Adult")

# 4.
a,b,c = 3,3,3
if a==b==c: print("Equilateral")
elif a==b or b==c or a==c: print("Isosceles")
else: print("Scalene")