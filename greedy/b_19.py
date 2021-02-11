'''
동빈나 그리디 우선순위 큐 프로그래머스 무지의 먹방 라이브
입력예제 [3,1,2],5 답 1
[8,6,4],15 답 2
'''

# 답

import heapq

def solution(food_times,k):
    if sum(food_times)<=k:
        return -1
    length=len(food_times)

    q=[]
    for i in range(length):
        heapq.heappush(q,(food_times[i],i+1))
    sum_value=0
    previous=0
    while sum_value+((q[0][0]-previous)*length)<=k:
        now=heapq.heappop(q)[0]
        sum_value+=(now-previous)*length
        length-=1
        previous=now
    result=sorted(q,key=lambda x:x[1])
    return result[(k-sum_value)%length][1]

print(solution([8,6,4],15))