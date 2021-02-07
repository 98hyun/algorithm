'''
동빈나 미래도시
플로이드워셜알고리즘

입력예제
5 7 노드 간선
1 2 거리 동일
1 3
1 4
2 4
3 4
3 5
4 5
4 5 5를 거쳐 4로 간다.
 
답 3
'''

n,m=map(int,input().split())
INF=int(1e9)
graph=[[INF]*(n+1) for _ in range(n+1)]

for i in range(1,n+1):
    for j in range(1,n+1):
        if i==j:
            graph[i][j]=0

for _ in range(m):
    a,b=map(int,input().split())
    graph[a][b]=1
    graph[b][a]=1

for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            graph[i][j]=min(graph[i][j],graph[i][k]+graph[k][j])

x,k=map(int,input().split())
dist=graph[1][k]+graph[k][x]
if dist==INF:
    print("-1")
else:
    print(dist)