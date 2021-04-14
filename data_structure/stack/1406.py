import sys
input=sys.stdin.readline
 
stk1 = list(input().strip())
stk2 = []
n = int(input())
while n>0:
    n-=1
    a=input().strip().split(' ')
    if a[0] == 'L':
        if stk1: stk2.append(stk1.pop())
        else: continue
    elif a[0] == 'D':
        if stk2: stk1.append(stk2.pop())
        else: continue
    elif a[0] == 'B':
        if stk1: stk1.pop()
        else: continue
    elif a[0] == 'P':
        stk1.append(a[1])
print(''.join(stk1+stk2[::-1]))