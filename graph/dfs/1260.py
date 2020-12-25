'''
DFS와 BFS 성공분류
시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
2 초	128 MB	112192	38868	22367	32.980%
문제
그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오. 단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고, 더 이상 방문할 수 있는 점이 없는 경우 종료한다. 정점 번호는 1번부터 N번까지이다.

입력
첫째 줄에 정점의 개수 N(1 ≤ N ≤ 1,000), 간선의 개수 M(1 ≤ M ≤ 10,000), 탐색을 시작할 정점의 번호 V가 주어진다. 다음 M개의 줄에는 간선이 연결하는 두 정점의 번호가 주어진다. 어떤 두 정점 사이에 여러 개의 간선이 있을 수 있다. 입력으로 주어지는 간선은 양방향이다.

출력
첫째 줄에 DFS를 수행한 결과를, 그 다음 줄에는 BFS를 수행한 결과를 출력한다. V부터 방문된 점을 순서대로 출력하면 된다.
'''

# 1. dfs/bfs 
# 2. 틀에 얽매이지 말것.

node,link,start=map(int,input().split())
graph=[[0]*(node+1) for _ in range(node+1)]
visited=[False]*(node+1)

for _ in range(link):
    a,b=map(int,input().split())
    graph[a][b]=1
    graph[b][a]=1

def dfs(start_node):
    visited[start_node]=True
    print(start_node,end=' ')
    for i in range(1,node+1):
        if not visited[i] and graph[start_node][i]==1:
            dfs(i)

def bfs(start_node):
    visited[start_node]=False
    queue=[start_node]
    while queue:
        q=queue.pop(0)
        print(q,end=' ')
        for i in range(1,node+1):
            if visited[i] and graph[q][i]==1:
                visited[i]=False
                queue.append(i)
    
dfs(start)
print()
bfs(start)

# 다른 풀이

n,m,v=map(int,input().split())
graph=[[] for _ in range(n+1)]
visited=[False]*(n+1)

for _ in range(m):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
    
for line in graph:
    line.sort()

def dfs(v):
    visited[v]=True
    print(v,end=' ')
    for i in graph[v]:
        if not visited[i]:
            visited[i]=True
            dfs(i)

def bfs(v):
    need_visited=[0]*(n+1)
    queue=[v]
    need_visited[v]=1
    
    while queue:
        q=queue.pop(0)
        print(q,end=' ')
        for i in graph[q]:
            if not need_visited[i]:
                queue.append(i)
                need_visited[i]=1
dfs(v)
print()
bfs(v)