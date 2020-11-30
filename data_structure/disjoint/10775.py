'''
공항 성공출처다국어분류
시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
1 초	256 MB	5701	2168	1574	39.291%
문제
오늘은 신승원의 생일이다.

박승원은 생일을 맞아 신승원에게 인천국제공항을 선물로 줬다.

공항에는 G개의 게이트가 있으며 각각은 1에서 G까지의 번호를 가지고 있다.

공항에는 P개의 비행기가 순서대로 도착할 예정이며, 당신은 i번째 비행기를 1번부터 gi (1 ≤ gi ≤ G) 번째 게이트중 하나에 영구적으로 도킹하려 한다. 비행기가 어느 게이트에도 도킹할 수 없다면 공항이 폐쇄되고, 이후 어떤 비행기도 도착할 수 없다.

신승원은 가장 많은 비행기를 공항에 도킹시켜서 박승원을 행복하게 하고 싶어한다. 승원이는 비행기를 최대 몇 대 도킹시킬 수 있는가?

입력
첫 번째 줄에는 게이트의 수 G (1 ≤ G ≤ 105)가 주어진다.

두 번째 줄에는 비행기의 수 P (1 ≤ P ≤ 105)가 주어진다.

이후 P개의 줄에 gi (1 ≤ gi ≤ G) 가 주어진다.

출력
승원이가 도킹시킬 수 있는 최대의 비행기 수를 출력한다.
'''

# 1. 맨처음 그냥 2 2 3 3 4 4에서 2에 들어왔으면 2에는 못들어와서 패스
#    3에 들어오고 패스 4에 들어오고 패스해서 3인줄 알았다.
# 2. disjoint-set 문제 인줄 몰랐다.
# 3. 풀이 키는 그냥 트리를 만들어 부모노드를 읽힐때 while 문으로 계속 쓰게 하면 선형탐색이 되니까
#    부모노드를 찾을 때 값을 할당해줘서 미리 트리를 줄이는 것이다.
# 4. 위 문제를 union-find 문제라고도 한다.

import sys
input=sys.stdin.readline

def find(n):
    if n==parent[n]:
        return n
    parent[n] = find(parent[n])
    return parent[n]
      
def union(x,y):
   x,y=find(x),find(y)
   parent[x]=y
   
g=int(input().strip())
p=int(input().strip())
planes=[int(input().strip()) for _ in range(p)]
parent=[i for i in range(g+1)]

count=0
for i in range(p):
    temp=find(planes[i]) 
    if temp== 0:
        break
    union(temp,temp-1)
    count+=1
print(count)



