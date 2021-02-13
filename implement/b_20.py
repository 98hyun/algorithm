'''
동빈나 럭키 스트레이트
입력예제 123402 답 LUCKY
7755 답 READY
'''

s=input()
n=len(s)

left=s[:n//2] 
right=s[n//2:]

left_sum=sum([int(i) for i in left])
right_sum=sum([int(i) for i in right])

if left_sum==right_sum:
    print('LUCKY')
else:
    print('READY')

# 답

n=input()
x=len(n)
summary=0

for i in range(x//2):
    summary+=int(n[i])
for i in range(x//2,x):
    summary-=int(n[i])

if summary==0:
    print('LUCKY')
else:
    print('READY')