'''
동빈나 전보
다익스트라 최단거리
입력예제
3 2 1 # 총 노드, 정보 수 , 채널
1 2 4 # 시작노드, 목적노드, 걸리는시간
1 3 2
답
2 4
'''

import heapq
import sys
input=sys.stdin.readline

INF=int(1e9)
n,m,c=map(int,input().strip().split())
distance=[INF]*(n+1)

graph=[[] for _ in range(n+1)]
for _ in range(m):
    i,j,k=map(int,input().strip().split())
    graph[i].append((j,k))

def dijkstra(start):
    q=[]
    heapq.heappush(q,(0,start))
    distance[start]=0
    while q:
        dist,now=heapq.heappop(q)
        if distance[now]<dist:
            continue
        for i in graph[now]:
            cost=dist+i[1]
            if cost<distance[i[0]]:
                distance[i[0]]=cost
                heapq.heappush(q,(cost,i[0]))

dijkstra(c)

count=0
max_dist=0
for d in distance:
    if d!=INF:
        count+=1
        max_dist=max(max_dist,d)
print(count-1,max_dist)