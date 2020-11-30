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

# 1. 그리디 , 동적계획법 문제.
# 2. 대각으로 가는게 가장 효율적인. -> 그리디
# 3. 동적계획법 끝내는 기술.오른쪽 대각이 가능하면 나머지는 무시해야한다.
# 4. dx,dy 사용 , switch 방법으로 중간 무시하게.
# 5. 함수는 지역변수를 사용한다. 그래서 전역변수로 고쳐줘야한다. 

import sys
input=sys.stdin.readline

r,c=map(int,input().strip().split())
maps=[list(input().strip()) for _ in range(r)]

dx=[-1,0,1]
dy=[1,1,1]
count=0

def dfs(x,y):
    global state,count
    if x==-1 or x==r:
        return
    if maps[x][y]=='x':
        return
    maps[x][y]='x'
    if y==c-1:
        state=True
        count+=1
        return
    for j in range(3):
        dfs(x+dx[j],y+dy[j])
        if state:
            return

for i in range(r):
    state=False
    dfs(i,0)
print(count)








