'''
단지번호붙이기 성공출처분류
시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
1 초	128 MB	70186	28263	17953	38.559%
문제
<그림 1>과 같이 정사각형 모양의 지도가 있다. 1은 집이 있는 곳을, 0은 집이 없는 곳을 나타낸다. 철수는 이 지도를 가지고 연결된 집의 모임인 단지를 정의하고, 단지에 번호를 붙이려 한다. 여기서 연결되었다는 것은 어떤 집이 좌우, 혹은 아래위로 다른 집이 있는 경우를 말한다. 대각선상에 집이 있는 경우는 연결된 것이 아니다. <그림 2>는 <그림 1>을 단지별로 번호를 붙인 것이다. 지도를 입력하여 단지수를 출력하고, 각 단지에 속하는 집의 수를 오름차순으로 정렬하여 출력하는 프로그램을 작성하시오.



입력
첫 번째 줄에는 지도의 크기 N(정사각형이므로 가로와 세로의 크기는 같으며 5≤N≤25)이 입력되고, 그 다음 N줄에는 각각 N개의 자료(0혹은 1)가 입력된다.

출력
첫 번째 줄에는 총 단지수를 출력하시오. 그리고 각 단지내 집의 수를 오름차순으로 정렬하여 한 줄에 하나씩 출력하시오.
'''

# 1. bfs/dfs
# 2. bfs는 가는게 아닌 오게하는것. bfs는 직접 가는것.
# 3. 조건 유의!  visited 과 graph 값의 조건을 항상 생각할 것.
# 4. 떨어져있는데 뭔가를 세라고 하면 그건 global 을 생각하는것.
# 5. global은 dfs에 유리 왜냐하면 직접 가야하니까 하지만, bfs는 함수를 1회만 실행시키니 안에서 count 가능.

n=int(input())
graph=[]

# visit
visited=[[0]*n for _ in range(n)]

# left,right,up,down
dx=[0,0,-1,1]
dy=[-1,1,0,0]

for _ in range(n):
    graph.append(list(map(int,input())))

def dfs(x,y):
    visited[x][y]=1
    global num
    if graph[x][y]==1:
        num+=1
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if 0<=nx<n and 0<=ny<n:
            if visited[nx][ny]==0 and graph[nx][ny]==1:
                dfs(nx,ny)

num=0
num_lst=[]
for i in range(n):
    for j in range(n):
        if visited[i][j]==0 and graph[i][j]==1:
            dfs(i,j)
            num_lst.append(num)
            num=0

print(len(num_lst))
for i in sorted(num_lst):
    print(i)


# bfs

n=int(input())
graph=[]

for _ in range(n):
    graph.append(list(map(int,input())))

dx=[0,0,-1,1]
dy=[1,-1,0,0]

visited=[[0]*n for _ in range(n)]
def bfs(x,y):
    visited[x][y]=1
    queue=[(x,y)]
    global num
    while queue:
        x,y=queue.pop(0)
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx and n>nx and 0<=ny and n>ny and graph[nx][ny]==1 and visited[nx][ny]==0:
                queue.append((nx,ny))
                visited[nx][ny]=1
                num+=1
num=1
num_lst=[]
for i in range(n):
    for j in range(n):
        if graph[i][j]==1 and visited[i][j]==0:
            bfs(i,j)
            num_lst.append(num)
            num=1

print(len(num_lst))
for i in sorted(num_lst):
    print(i)