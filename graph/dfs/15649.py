'''
N과 M (1) 성공분류
시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
1 초	512 MB	25110	15189	10293	60.214%
문제
자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.

1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열
입력
첫째 줄에 자연수 N과 M이 주어진다. (1 ≤ M ≤ N ≤ 8)

출력
한 줄에 하나씩 문제의 조건을 만족하는 수열을 출력한다. 중복되는 수열을 여러 번 출력하면 안되며, 각 수열은 공백으로 구분해서 출력해야 한다.

수열은 사전 순으로 증가하는 순서로 출력해야 한다.
'''

# 1. 순열과 조합
# 2. 그 안에는 dfs? dfs 공부하고 다시 .

# from itertools import permutations as perm

# n,m=map(int,input().split())
# arr=range(1,n+1)

# brr=list(perm(arr,m))
# for b in brr:
#     print(*b)
    # print(' '.join(map(str,b)))

# dfs 

n,m=map(int,input().split())

graph=[i for i in range(1,n+1)]
visited=[False]*(n+1)
arr=[]

def dfs(count):
    if count==m:
        print(*arr)
        return
    for i in range(1,n+1):
        if visited[i]:
            continue
        visited[i]=True
        arr.append(i)
        dfs(count+1)
        visited[i]=False
        arr.pop()

dfs(0)