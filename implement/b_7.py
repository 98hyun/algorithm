# 0. 동빈나 책. 게임 개발
# 1. 시뮬레이션
# 입력예제 
# 4 4
# 1 1 0
# 1 1 1 1
# 1 0 0 1
# 1 1 0 1
# 1 1 1 1

n,m=map(int,input().split())
x,y,loc=map(int,input().split())
# 북,동,남,서
dx=[-1,0,1,0]
dy=[0,1,0,-1]

visited=[[0]*m for _ in range(n)]
graph=[]
for i in range(n):
    graph.append(list(map(int,input().split())))
visited[x][y]=1

# 1단계 왼쪽돌기
def turn_left():
    global loc
    loc+=1
    if loc==4:
        loc=0

# 2단계 simulation
count=1
turn_time=0
while 1:
    turn_left()
    print(loc)
    nx=x+dx[loc]
    ny=y+dy[loc]
    if not visited[nx][ny] and not graph[nx][ny]:
        visited[nx][ny]=1
        x,y=nx,ny
        count+=1
        turn_time=0
        continue
    else:
        turn_time+=1
    if turn_time==4:
        nx=x-dx[loc]
        ny=y-dy[loc]
        if not graph[nx][ny]:
            x,y=nx,ny
        else:
            break
        turn_time=0

print(count)