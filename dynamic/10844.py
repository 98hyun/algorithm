'''
쉬운 계단 수 성공분류
시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
1 초	256 MB	67788	20469	14689	28.330%
문제
45656이란 수를 보자.

이 수는 인접한 모든 자리수의 차이가 1이 난다. 이런 수를 계단 수라고 한다.

세준이는 수의 길이가 N인 계단 수가 몇 개 있는지 궁금해졌다.

N이 주어질 때, 길이가 N인 계단 수가 총 몇 개 있는지 구하는 프로그램을 작성하시오. (0으로 시작하는 수는 없다.)

입력
첫째 줄에 N이 주어진다. N은 1보다 크거나 같고, 100보다 작거나 같은 자연수이다.

출력
첫째 줄에 정답을 1,000,000,000으로 나눈 나머지를 출력한다.
'''

# 1. dynamic programming
# 2. memorization

import sys
input=sys.stdin.readline

n=int(input().strip())

dp=[[0]*10 for _ in range(101)]
for i in range(1,10):
    dp[1][i]=1
for i in range(2,n+1):
    for j in range(10):
        if j==0:
            dp[i][j]=dp[i-1][j+1]
        elif j==9:
            dp[i][j]=dp[i-1][j-1]
        else:
            dp[i][j]=dp[i-1][j-1]+dp[i-1][j+1]
print(sum(dp[n])%int(1e9))







        
