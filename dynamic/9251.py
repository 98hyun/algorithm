'''
LCS 분류
시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
1 초	256 MB	27092	11092	8186	40.595%
문제
LCS(Longest Common Subsequence, 최장 공통 부분 수열)문제는 두 수열이 주어졌을 때, 모두의 부분 수열이 되는 수열 중 가장 긴 것을 찾는 문제이다.

예를 들어, ACAYKP와 CAPCAK의 LCS는 ACAK가 된다.

입력
첫째 줄과 둘째 줄에 두 문자열이 주어진다. 문자열은 알파벳 대문자로만 이루어져 있으며, 최대 1000글자로 이루어져 있다.

출력
첫째 줄에 입력으로 주어진 두 문자열의 LCS의 길이를 출력한다.
'''

# 1. LCS(longest common subsequence)
# 2. 규칙이 안보일때에는 2차원도 생각.

m = list(input())
n = list(input())
m_len = len(m)
n_len = len(n)
dp = [[0] * (n_len + 1) for i in range(m_len + 1)]
for i in range(m_len):
    for j in range(n_len):
        if m[i] == n[j]:
            dp[i + 1][j + 1] = dp[i][j] + 1
        else:
            dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j])
print(dp[m_len][n_len])