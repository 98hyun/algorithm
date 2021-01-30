# 0. 동빈나 책. 상하좌우
# 1. 구현
# 입력예제 
# 5
# R R R U D D

n=int(input())

arr=input().split()

x,y=1,1
# R L U D
dx=[0,0,-1,1]
dy=[1,-1,0,0]

move_types=['R','L','U','D']

for s in arr:
    for i in range(4):
        if s==move_types[i]:
            nx=x+dx[i]
            ny=y+dy[i]
    if nx<1 or ny<1 or nx>n or ny>n:
        continue
    x,y=nx,ny
print(x,y)