'''
한 줄로 서기 성공분류
시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
2 초	128 MB	5380	2893	2476	56.337%
문제
N명의 사람들은 매일 아침 한 줄로 선다. 이 사람들은 자리를 마음대로 서지 못하고 오민식의 지시대로 선다.

어느 날 사람들은 오민식이 사람들이 줄 서는 위치를 기록해 놓는다는 것을 알았다. 그리고 아침에 자기가 기록해 놓은 것과 사람들이 줄을 선 위치가 맞는지 확인한다.

사람들은 자기보다 큰 사람이 왼쪽에 몇 명 있었는지만을 기억한다. N명의 사람이 있고, 사람들의 키는 1부터 N까지 모두 다르다.

각 사람들이 기억하는 정보가 주어질 때, 줄을 어떻게 서야 하는지 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 사람의 수 N이 주어진다. N은 10보다 작거나 같은 자연수이다. 둘째 줄에는 키가 1인 사람부터 차례대로 자기보다 키가 큰 사람이 왼쪽에 몇 명이 있었는지 주어진다. i번째 수는 0보다 크거나 같고, N-i보다 작거나 같다.
'''

# 1. 순서대로 가면서 넣는것이다.
# 2. 앞의 빈자리수를 체크하면서 count값을 키워준다.
# 3. 예외로 빈자리수를 체크는 하지만 count가 안올라가게 해야한다.
# 4. 그래서 else 대신 elif 를 쓴다.

import sys
input=sys.stdin.readline

n=int(input().strip())
arr=list(map(int,input().strip().split()))

answer=[0]*n

for i in range(1,n+1):
    count=0
    for j in range(n):
        if count==arr[i-1] and not answer[j]:
            answer[j]=i
            break
        elif not answer[j]:
            count+=1
print(*answer)

# 신기한 풀이

n=int(input())
a=input().split(' ')
a=list(map(int,a))
b=list()

for i in range(n):
    b.insert(a[n-1-i],n-i)
for j in b:
    print(j,end=' ')

    
        
