# 1.
for i in range(1,11): print(i)

# 2. 
n = 5
i = 1
while i<=10:
    print(n, "x", i, "=", n*i)
    i += 1

# 3. 
n = 3
for i in range(1, n+1):
    print(" "*(n-i) + "*"* (2*i-1))

# 4.
n = 20
for num in range(2,n+1):
    if all(num%i!=0 for i in range(2,int(num**0.5)+1)):
        print(num,end=" ")

# 5.
def fact(n):
    return 1 if n==0 else n*fact(n-1)
print(fact(5))

# 6.
def sum_all(*args):
    return sum(args)
print(sum_all(1,2,3,4))

# 7. 
for i in range(1,11):
    if i==5: continue
    print(i)

# 8. 
for i in range(1,11):
    if i==7: break
    print(i)

# 9. 
def hanoi(n, src, aux, dest):
    if n==1:
        print(f"Move {src}->{dest}")
        return
    hanoi(n-1, src, dest, aux)
    print(f"Move {src}->{dest}")
    hanoi(n-1, aux, src, dest)
hanoi(3,'A','B','C')

# 10.
board = [" "]*9
def print_board():
    for i in range(0,9,3):
        print(board[i], board[i+1], board[i+2])

player = "X"
for _ in range(9):
    pos = int(input("Enter position (0-8): "))
    if board[pos]==" ":
        board[pos]=player
        print_board()
        player = "O" if player=="X" else "X"