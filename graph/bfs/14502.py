'''
연구소 성공분류
시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
2 초	512 MB	35320	20173	10936	54.332%
문제
인체에 치명적인 바이러스를 연구하던 연구소에서 바이러스가 유출되었다. 다행히 바이러스는 아직 퍼지지 않았고, 바이러스의 확산을 막기 위해서 연구소에 벽을 세우려고 한다.

연구소는 크기가 N×M인 직사각형으로 나타낼 수 있으며, 직사각형은 1×1 크기의 정사각형으로 나누어져 있다. 연구소는 빈 칸, 벽으로 이루어져 있으며, 벽은 칸 하나를 가득 차지한다. 

일부 칸은 바이러스가 존재하며, 이 바이러스는 상하좌우로 인접한 빈 칸으로 모두 퍼져나갈 수 있다. 새로 세울 수 있는 벽의 개수는 3개이며, 꼭 3개를 세워야 한다.

예를 들어, 아래와 같이 연구소가 생긴 경우를 살펴보자.

2 0 0 0 1 1 0
0 0 1 0 1 2 0
0 1 1 0 1 0 0
0 1 0 0 0 0 0
0 0 0 0 0 1 1
0 1 0 0 0 0 0
0 1 0 0 0 0 0
이때, 0은 빈 칸, 1은 벽, 2는 바이러스가 있는 곳이다. 아무런 벽을 세우지 않는다면, 바이러스는 모든 빈 칸으로 퍼져나갈 수 있다.

2행 1열, 1행 2열, 4행 6열에 벽을 세운다면 지도의 모양은 아래와 같아지게 된다.

2 1 0 0 1 1 0
1 0 1 0 1 2 0
0 1 1 0 1 0 0
0 1 0 0 0 1 0
0 0 0 0 0 1 1
0 1 0 0 0 0 0
0 1 0 0 0 0 0
바이러스가 퍼진 뒤의 모습은 아래와 같아진다.

2 1 0 0 1 1 2
1 0 1 0 1 2 2
0 1 1 0 1 2 2
0 1 0 0 0 1 2
0 0 0 0 0 1 1
0 1 0 0 0 0 0
0 1 0 0 0 0 0
벽을 3개 세운 뒤, 바이러스가 퍼질 수 없는 곳을 안전 영역이라고 한다. 위의 지도에서 안전 영역의 크기는 27이다.

연구소의 지도가 주어졌을 때 얻을 수 있는 안전 영역 크기의 최댓값을 구하는 프로그램을 작성하시오.

입력
첫째 줄에 지도의 세로 크기 N과 가로 크기 M이 주어진다. (3 ≤ N, M ≤ 8)

둘째 줄부터 N개의 줄에 지도의 모양이 주어진다. 0은 빈 칸, 1은 벽, 2는 바이러스가 있는 위치이다. 2의 개수는 2보다 크거나 같고, 10보다 작거나 같은 자연수이다.

빈 칸의 개수는 3개 이상이다.

출력
첫째 줄에 얻을 수 있는 안전 영역의 최대 크기를 출력한다.
'''

# 1. 조합과 dfs/bfs 사용.
# 2. 벽을 세우는 모든 조건 돌면서 확인.
# 3. 벽이 세워졌을 때 바이러스를 돌리고 안전한 최댓값 비교.

n,m=map(int,input().split())
graph=[]

for _ in range(n):
    graph.append(list(map(int,input().split())))

dx=[-1,1,0,0]
dy=[0,0,-1,1]

max_values=0

def bfs():
    global max_values
    copy_graph=[[0]*m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            copy_graph[i][j]=graph[i][j]

    virus_list=[]
    for i in range(n):
        for j in range(m):
            if copy_graph[i][j]==2:
                virus_list.append((i,j))
    while virus_list:
        x,y=virus_list.pop(0)
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx>=0 and nx<n and ny>=0 and ny<m:
                if copy_graph[nx][ny]==0:
                    copy_graph[nx][ny]=2
                    virus_list.append((nx,ny))
    result=0
    for i in range(n):
        for j in range(m):
            if copy_graph[i][j]==0:
                result+=1
    max_values=max(result,max_values)

def wall(count):
    if count==3:
        bfs()
        return
    else:
        for i in range(n):
            for j in range(m):
                if graph[i][j]==0:
                    graph[i][j]=1
                    wall(count+1)
                    graph[i][j]=0

wall(0)
print(max_values)

# 다른 풀이 dfs

# import sys
# input=sys.stdin.readline
# import copy

# n,m=map(int,input().strip().split())
# graph=[]
# for _ in range(n):
#     graph.append(list(map(int,input().strip().split())))

# dr=[-1,1,0,0]
# dc=[0,0,1,-1]

# max_value=0

# def select_wall(start,count):
#     global max_value
#     if count==3:
#         copy_graph=copy.deepcopy(graph)
#         for r in range(n):
#             for c in range(m):
#                 spread_virus(r,c,copy_graph)
#         safe_counts=sum([i.count(0) for i in copy_graph])
#         max_value=max(max_value,safe_counts)
#         return 
#     else:
#         for i in range(n*m):
#             r=i//m
#             c=i%m
#             if graph[r][c]==0:
#                 graph[r][c]=1
#                 select_wall(i,count+1)
#                 graph[r][c]=0

# def spread_virus(r,c,copy_graph):
#     if copy_graph[r][c]==2:
#         for i in range(4):
#             nr=r+dr[i]
#             nc=c+dc[i]
#             if nr>=0 and nr<n and nc>=0 and nc<m:
#                 if copy_graph[nr][nc]==0:
#                     copy_graph[nr][nc]=2
#                     spread_virus(nr,nc,copy_graph)

# select_wall(0,0)
# print(max_value)