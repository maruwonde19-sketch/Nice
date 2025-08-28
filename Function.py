# 1
def square():
    n = int(input("Enter a number: "))
    return n * n

result = square()
print("Square is:", result)

# 2.
def is_palindrome(s): return s==s[::-1]

# 3.
import time
def timer(func):
    def wrapper(*args, **kwargs):
        start=time.time()
        result=func(*args, **kwargs)
        print("Execution time:", time.time()-start)
        return result
    return wrapper

@timer
def slow_func():
    time.sleep(1)
    return "Done"

print(slow_func())

# 4.
def prime_gen():
    num = 2
    while True:
        if all(num%i!=0 for i in range(2,int(num**0.5)+1)):
            yield num
        num += 1

gen = prime_gen()
for _ in range(10):
    print(next(gen))