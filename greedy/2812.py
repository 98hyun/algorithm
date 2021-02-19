'''
크게 만들기 출처다국어분류
시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
1 초	128 MB	9916	1978	1474	22.786%
문제
N자리 숫자가 주어졌을 때, 여기서 숫자 K개를 지워서 얻을 수 있는 가장 큰 수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 N과 K가 주어진다. (1 ≤ K < N ≤ 500,000)

둘째 줄에 N자리 숫자가 주어진다. 이 수는 0으로 시작하지 않는다.

출력
입력으로 주어진 숫자에서 K개를 지웠을 때 얻을 수 있는 가장 큰 수를 출력한다.

예제 입력 1 
4 2
1924
예제 출력 1 
94
'''

# 1. greedy
# 2. programmers 에서 본 문제. 큰수 만들기.

n,k=map(int,input().split())

s=input()
res=[s[0]]

for i in range(1,n):
    while res and res[-1]<s[i] and k>0:
        res.pop()
        k-=1
    res.append(s[i])
res=res[:-k] if k>0 else res
print(''.join(res))