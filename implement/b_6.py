# 0. 동빈나 책. 왕실의 나이트
# 1. 구현
# 입력예제 
# a1

s=input()
x=ord(s[0])-96
y=int(s[1])

print(x,y)
dx=[2,2,-2,-2,1,-1,1,-1]
dy=[-1,1,-1,1,2,2,-2,-2]

count=0
for i in range(8):
    nx=x+dx[i]
    ny=y+dy[i]
    if nx<1 or ny<1 or nx>8 or ny>8:
        continue
    count+=1
print(count)