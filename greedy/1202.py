'''
보석 도둑 성공출처다국어분류
시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
1 초	256 MB	11414	2713	1918	23.542%
문제
세계적인 도둑 상덕이는 보석점을 털기로 결심했다.

상덕이가 털 보석점에는 보석이 총 N개 있다. 각 보석은 무게 Mi와 가격 Vi를 가지고 있다. 상덕이는 가방을 K개 가지고 있고, 각 가방에 담을 수 있는 최대 무게는 Ci이다. 가방에는 최대 한 개의 보석만 넣을 수 있다.

상덕이가 훔칠 수 있는 보석의 최대 가격을 구하는 프로그램을 작성하시오.

입력
첫째 줄에 N과 K가 주어진다. (1 ≤ N, K ≤ 300,000)

다음 N개 줄에는 각 보석의 정보 Mi와 Vi가 주어진다. (0 ≤ Mi, Vi ≤ 1,000,000)

다음 K개 줄에는 가방에 담을 수 있는 최대 무게 Ci가 주어진다. (1 ≤ Ci ≤ 100,000,000)

모든 숫자는 양의 정수이다.

출력
첫째 줄에 상덕이가 훔칠 수 있는 보석 가격의 합의 최댓값을 출력한다.
'''

# 1. 수가 엄청 크기 때문에 계속 비교할 수가 없다. 그때문에 효율적인 데이터구조를 골라야한다. -> 우선순위 큐
# 2. 보석이 무거워도 값이 비싸면 챙긴다. 
# 3. 허용량이 적은 가방에 값비싼 것부터 챙기면 된다. -> 그리디
# 4. 가방의 수가 값을 정한다. -> 가방이 기준.

import heapq
import sys
input=sys.stdin.readline

N,K=map(int,input().strip().split())
jewelry=[]
bags=[]
for _ in range(N):
    a,b=map(int,input().strip().split())
    jewelry.append((a,b))
jewelry.sort(key=lambda x:x[0],reverse=True)
for _ in range(K):
    c=int(input().strip())
    bags.append(c)
bags.sort()
heap=[]
result=0
for bag in bags:
    while jewelry and bag>=jewelry[-1][0]:
        heapq.heappush(heap,-jewelry.pop()[1])
    if heap:
        result-=heapq.heappop(heap)
print(result)
    
