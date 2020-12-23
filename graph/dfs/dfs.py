'''
dfs 기본정의
'''

graph=[
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]
visited=[False]*9
result=[]
def dfs(graph,start_node,visited):
    visited[start_node]=True
    result.append(str(start_node))
    for i in graph[start_node]:
        if not visited[i]:
            visited[i]=True
            dfs(graph,i,visited)

dfs(graph,1,visited)
print(' '.join(result))