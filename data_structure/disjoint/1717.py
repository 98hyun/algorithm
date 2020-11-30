'''
집합의 표현 성공스페셜 저지분류
시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
2 초	128 MB	33408	11242	6853	30.060%
문제
초기에 {0}, {1}, {2}, ... {n} 이 각각 n+1개의 집합을 이루고 있다. 여기에 합집합 연산과, 두 원소가 같은 집합에 포함되어 있는지를 확인하는 연산을 수행하려고 한다.

집합을 표현하는 프로그램을 작성하시오.

입력
첫째 줄에 n(1≤n≤1,000,000), m(1≤m≤100,000)이 주어진다. m은 입력으로 주어지는 연산의 개수이다. 다음 m개의 줄에는 각각의 연산이 주어진다. 합집합은 0 a b의 형태로 입력이 주어진다. 이는 a가 포함되어 있는 집합과, b가 포함되어 있는 집합을 합친다는 의미이다. 두 원소가 같은 집합에 포함되어 있는지를 확인하는 연산은 1 a b의 형태로 입력이 주어진다. 이는 a와 b가 같은 집합에 포함되어 있는지를 확인하는 연산이다. a와 b는 n 이하의 자연수 또는 0이며 같을 수도 있다.

출력
1로 시작하는 입력에 대해서 한 줄에 하나씩 YES/NO로 결과를 출력한다. (yes/no 를 출력해도 된다)
'''

# 1. disjoint-set 문제.

import sys
input=sys.stdin.readline

def find(n):
    if n==parent[n]:
        return n
    parent[n]=find(parent[n])
    return parent[n]
      
def union(x,y):
    x,y=find(x),find(y)
    if x<y:
        parent[y]=x
    else:
        parent[x]=y
   
n,m=map(int,input().strip().split())
parent={i:i for i in range(n+1)}

while m>0:
    m-=1
    a,b,c=map(int,input().strip().split())
    if not a:
        union(b,c)
    else:
        if find(b)==find(c):
            print('YES')
        else:
            print('NO')



