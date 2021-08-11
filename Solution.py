# Enter your code here. Read input from STDIN. Print output to STDOUT
n, m = list(map(int,input().split()))
ns = list(map(int,input().split()))
h = set(map(int,input().split()))
s = set(map(int,input().split()))
r = 0
for i in ns:
    if i in h:
        r += 1
    elif i in s:
        r -= 1

print(r)
