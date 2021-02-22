'''
강의실 배정 실패분류
시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
1 초	256 MB	7091	2120	1490	29.256%
문제
수강신청의 마스터 김종혜 선생님에게 새로운 과제가 주어졌다. 

김종혜 선생님한테는 Si에 시작해서 Ti에 끝나는 N개의 수업이 주어지는데, 최소의 강의실을 사용해서 모든 수업을 가능하게 해야 한다. 

참고로, 수업이 끝난 직후에 다음 수업을 시작할 수 있다. (즉, Ti ≤ Sj 일 경우 i 수업과 j 수업은 같이 들을 수 있다.)

수강신청 대충한 게 찔리면, 선생님을 도와드리자!

입력
첫 번째 줄에 N이 주어진다. (1 ≤ N ≤ 200,000)

이후 N개의 줄에 Si, Ti가 주어진다. (1 ≤ Si < Ti ≤ 109)

출력
강의실의 개수를 출력하라.

예제 입력 1 
3
1 3
2 4
3 5
예제 출력 1 
2
'''

# 1. 그리디
# 2. 마지막 시간을 비교하는건 알았는데 시간초과가 있다. 
# 일단, big(o)로 대충 보고 만약 시간초과가 의심이 된다면 
# 1번 sys input 바꾸기
# 2번 알고리즘의 문제. 그래서 log(n)밖에 안된다. log(n)은 이진탐색 혹은 list에서 우선순위 큐밖에없다.

import heapq
import sys
input=sys.stdin.readline

n=int(input().strip())
timetable=[list(map(int,input().strip().split())) for _ in range(n)]
timetable.sort(key=lambda x:x[0])

q=[]
heapq.heappush(q,timetable[0][1])

for i in range(1,n):
    if q[0]>timetable[i][0]:
        heapq.heappush(q,timetable[i][1])
    else:
        heapq.heappop(q)
        heapq.heappush(q,timetable[i][1])
print(len(q))