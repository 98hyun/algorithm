'''
정수 삼각형 성공출처다국어분류
시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
2 초	128 MB	38379	22493	16704	58.751%
문제
        7
      3   8
    8   1   0
  2   7   4   4
4   5   2   6   5
위 그림은 크기가 5인 정수 삼각형의 한 모습이다.

맨 위층 7부터 시작해서 아래에 있는 수 중 하나를 선택하여 아래층으로 내려올 때, 이제까지 선택된 수의 합이 최대가 되는 경로를 구하는 프로그램을 작성하라. 아래층에 있는 수는 현재 층에서 선택된 수의 대각선 왼쪽 또는 대각선 오른쪽에 있는 것 중에서만 선택할 수 있다.

삼각형의 크기는 1 이상 500 이하이다. 삼각형을 이루고 있는 각 수는 모두 정수이며, 범위는 0 이상 9999 이하이다.

입력
첫째 줄에 삼각형의 크기 n(1 ≤ n ≤ 500)이 주어지고, 둘째 줄부터 n+1번째 줄까지 정수 삼각형이 주어진다.

출력
첫째 줄에 합이 최대가 되는 경로에 있는 수의 합을 출력한다.
'''

# 1. dynamic programming
# 2. 0,1 만 보면 되는 문제.
# 3. 고칠점 : 대신 len(dp[i])를 하면 len 함수를 불러오면서 늦으니까
# 변수 m에 2부터 1씩 증가 시키는 것도 좋다. 

import sys
input=sys.stdin.readline

n=int(input().strip())
dp=[0]
for _ in range(n):
    dp.append(list(map(int,input().strip().split())))
for i in range(2,n+1):
    for j in range(len(dp[i])-1):
        if j==0:
            dp[i][0]+=dp[i-1][0]
        elif i==j:
            dp[i][j]+=dp[i-1][j-1]
        else:
            dp[i][j]+=max(dp[i-1][j],dp[i-1][j-1])
print(max(dp[-1]))


# 다른 방법.

import sys
input=sys.stdin.readline

n=int(input().strip())
dp=[]
m=2
for _ in range(n):
    dp.append(list(map(int,input().strip().split())))
for i in range(1,n):
    for j in range(m):
        if j==0:
            dp[i][0]+=dp[i-1][0]
        elif i==j:
            dp[i][j]+=dp[i-1][j-1]
        else:
            dp[i][j]+=max(dp[i-1][j],dp[i-1][j-1])
    m+=1
print(max(dp[-1]))