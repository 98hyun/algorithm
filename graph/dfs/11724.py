'''
연결 요소의 개수 성공분류
시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
3 초	512 MB	35403	17238	11194	45.794%
문제
방향 없는 그래프가 주어졌을 때, 연결 요소 (Connected Component)의 개수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 정점의 개수 N과 간선의 개수 M이 주어진다. (1 ≤ N ≤ 1,000, 0 ≤ M ≤ N×(N-1)/2) 둘째 줄부터 M개의 줄에 간선의 양 끝점 u와 v가 주어진다. (1 ≤ u, v ≤ N, u ≠ v) 같은 간선은 한 번만 주어진다.

출력
첫째 줄에 연결 요소의 개수를 출력한다.
'''

# 1. dfs 
# 2. 항상 sys.setrecursionlimit 생각하기 
# 3. input도 느릴 수 있다.

import sys
input=sys.stdin.readline
sys.setrecursionlimit(10000)

n,m=map(int,input().strip().split())

graph=[[0]*(n+1) for _ in range(n+1)]

for _ in range(m):
    a,b=map(int,input().strip().split())
    graph[a][b]=1
    graph[b][a]=1

visited=[False]*(n+1)

def dfs(x):
    visited[x]=True
    for i in range(1,n+1):
        if not visited[i] and graph[x][i]:
            dfs(i)
 
count=0
for i in range(1,n+1):
    if not visited[i]:
        dfs(i)
        count+=1

print(count)