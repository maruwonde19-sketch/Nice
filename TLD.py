# 1.
t = (1,2,3,4)
count = sum(1 for _ in t)
print(count)

# 2.
print(max(t), min(t))

# 3.
lst = [1,2,2,3,4,4]
lst = list(set(lst))
print(lst)

# 4.
lst = [1,2,3,4,5]
squared = [x**2 for x in lst]
print(squared)

# 5.
d1 = {"a":1, "b":2}
d2 = {"c":3, "d":4}
merged = {**d1, **d2}
print(merged)

# 6.
d = {'a':1, 'b':2, 'c':3}
swapped = {v:k for k,v in d.items()}
print(swapped)

# 7.
def fib(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fib(n-1, memo) + fib(n-2, memo)
    return memo[n]

print(fib(10))

# 8.
n = 20
triplets = [(a,b,c) for a in range(1,n) for b in range(a,n) for c in range(b,n) if a*a+b*b==c*c]
print(triplets)

# 9.
cart = {}
def add_item(item, price):
    cart[item] = price
def remove_item(item):
    cart.pop(item, None)
def total():
    return sum(cart.values())

add_item("apple", 3)
add_item("milk", 2)
print(total())

# 10.
from collections import OrderedDict
class LRUCache:
    def __init__(self, max_size):
        self.cache = OrderedDict()
        self.max_size = max_size
    def get(self, key):
        if key in self.cache:
            self.cache.move_to_end(key)
            return self.cache[key]
        return -1
    def put(self, key, value):
        self.cache[key] = value
        self.cache.move_to_end(key)
        if len(self.cache) > self.max_size:
            self.cache.popitem(last=False)

cache = LRUCache(2)
cache.put(1,1); cache.put(2,2)
print(cache.get(1))
cache.put(3,3)
print(cache.get(2))  # evicted