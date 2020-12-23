'''
bfs 기본정의
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

def bfs(graph,start_node,visited):
    result.append(str(start_node))
    visited[start_node]=True
    need_visited=[start_node]
    while need_visited:
        p=need_visited.pop(0)
        for i in graph[p]:
            if not visited[i]:
                visited[i]=True
                result.append(str(i))
                need_visited.append(i)

bfs(graph,1,visited)
print(' '.join(result))