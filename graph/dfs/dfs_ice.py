'''
# 동빈나 음료수 얼려먹기

N*M 크기의 얼음 틀이 있습니다. 구멍이 뚫려있는 부분은 0, 칸막이가 존재하는 부분은 1로 표시됩니다.
구멍이 뚫려 있는 부분끼리는 상,하,좌,우로 붙어 있는 경우 연결되었다고 가정합니다.
얼음틀의 모양이 주어졌을때, 생성되는 아이스크림의 개수를 구하시오. 다음의 얼음틀에서는 
3개의 아이스크림이 생성됩니다.

예시

4 5 
00110
00011
00110
00110 

답 : 3개
'''


n,m=map(int,input().split())

graph=[]
for _ in range(n):
    graph.append(list(map(int,input())))

def dfs(x,y):
    if x<=-1 or x>=n or y<=-1 or y>=m:
        return False
    if graph[x][y]==0:
        graph[x][y]=1
        dfs(x-1,y)
        dfs(x+1,y)
        dfs(x,y-1)
        dfs(x,y+1)
        return True
    return False

count=0
for i in range(n):
    for j in range(m):
        if dfs(i,j):
            count+=1
print(count)
