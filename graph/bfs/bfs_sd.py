'''
# 동빈나 미로탈출

동빈이는 N*M 크기의 미로에 갇혔습니다. 미로에는 여러마리의 괴물이 있어 이를 피해 탈출해야합니다.
동빈이의 위치는 (1,1) 이고, 미로의 출구는 (N,M)에 존재하며 한번에 한칸 이동할 수 있습니다.
이때 괴물이 있는 부분은 0으로, 없는 부분은 1로 표시됩니다. 미로는 반드시 탈출할 수 있도록 주어집니다.
동빈이가 탈출하기위한 움직여야하는 최소 칸의 개수를 답하시오. 칸을 셀때는 시작과 끝을 포함해서 셉니다.

예시

5 6
101010
111111
000001
111111
111111

답 : 10칸.
'''


n,m=map(int,input().split())

graph=[]
for _ in range(n):
    graph.append(list(map(int,input())))

def bfs(x,y):
    queue=[]
    queue.append((x,y))
    while queue:
        x,y=queue.pop(0)
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx>=n or nx<=-1 or ny>=m or ny<=-1:
                continue
            if graph[nx][ny]==0:
                continue
            if graph[nx][ny]==1:
                graph[nx][ny]+=graph[x][y]
                queue.append((nx,ny))
    return graph[n-1][m-1]

dx=[-1,1,0,0]
dy=[0,0,-1,1]

print(bfs(0,0))
