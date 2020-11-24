'''
행렬 성공분류
시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
2 초	128 MB	7983	3112	2537	40.302%
문제
0과 1로만 이루어진 행렬 A와 행렬 B가 있다. 이때, 행렬 A를 행렬 B로 바꾸는데 필요한 연산의 횟수의 최솟값을 구하는 프로그램을 작성하시오.

행렬을 변환하는 연산은 어떤 3*3크기의 부분 행렬에 있는 모든 원소를 뒤집는 것이다. (0 -> 1, 1 -> 0)

입력
첫째 줄에 행렬의 크기 N M이 주어진다. N과 M은 50보다 작거나 같은 자연수이다. 둘째 줄부터 N개의 줄에는 행렬 A가 주어지고, 그 다음줄부터 N개의 줄에는 행렬 B가 주어진다.

출력
첫째 줄에 문제의 정답을 출력한다. 만약 A를 B로 바꿀 수 없다면 -1을 출력한다.
'''

# 1. 3x3. 좌측 상단부터 3개까지만 되고 3x5 같은 경우는 col=3 에서만 조절할 수 있다.
# 2. 그러다보니 3보다 작은 행렬은 직접 확인 할 수 밖에 없다.
# -> 그리디는 마지막 2개 col은 전 col로만 할 수 있으니 그 상단 점을 그리디라고 한것 같다. 완전탐색 느낌이 난다.

import sys
input=sys.stdin.readline

n,m=map(int,input().strip().split())
A=[[int(a) for a in input().strip()] for _ in range(n)]
B=[[int(a) for a in input().strip()] for _ in range(n)]
            
if n>=3 and m>=3:
    count=0
    for i in range(n-2):
        for j in range(m-2):
            if A[i][j]!=B[i][j]:
                count+=1
                for k in range(i,i+3):
                    for l in range(j,j+3):
                        A[k][l]=1-A[k][l]
    for i in range(n):
        for j in range(m):
            if A[i][j]!=B[i][j]:
                count=-1
                break
    print(count)
else:
    count=0
    for i in range(n):
        for j in range(m):
            if A[i][j]!=B[i][j]:
                count=-1
    print(count)
