'''
통계학 성공분류
시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
2 초	256 MB	35299	8152	6675	26.727%
문제
수를 처리하는 것은 통계학에서 상당히 중요한 일이다. 통계학에서 N개의 수를 대표하는 기본 통계값에는 다음과 같은 것들이 있다. 단, N은 홀수라고 가정하자.

산술평균 : N개의 수들의 합을 N으로 나눈 값
중앙값 : N개의 수들을 증가하는 순서로 나열했을 경우 그 중앙에 위치하는 값
최빈값 : N개의 수들 중 가장 많이 나타나는 값
범위 : N개의 수들 중 최댓값과 최솟값의 차이
N개의 수가 주어졌을 때, 네 가지 기본 통계값을 구하는 프로그램을 작성하시오.

입력
첫째 줄에 수의 개수 N(1 ≤ N ≤ 500,000)이 주어진다. 그 다음 N개의 줄에는 정수들이 주어진다. 입력되는 정수의 절댓값은 4,000을 넘지 않는다.

출력
첫째 줄에는 산술평균을 출력한다. 소수점 이하 첫째 자리에서 반올림한 값을 출력한다.

둘째 줄에는 중앙값을 출력한다.

셋째 줄에는 최빈값을 출력한다. 여러 개 있을 때에는 최빈값 중 두 번째로 작은 값을 출력한다.

넷째 줄에는 범위를 출력한다.
'''

# 1. 정렬? 
# 내가 봤을 땐, 효율적인 방법은 library를 가져오는 것. 기본 라이브러리 중에 statistics 가 있다.
# 대부분의 답은 Counter를 사용했고, 이번엔 zip을 이용했다. 
# 원래 dictionary는 순서가 없지만, 어느 버전부터

def mean(arr,n):
    return round(sum(arr)/n)

def median(arr,n):
    return arr[n//2]

def mode(arr,n):
    mode_dict=dict(zip(arr,[0]*n))
    for i in arr:
        mode_dict[i]+=1
    modes=[k for k,v in mode_dict.items() if v==max(mode_dict.values())]
    # modes.sort()
    return modes[0] if len(modes)==1 else modes[1]
        
def scope(arr):
    return arr[-1]-arr[0]

import sys
input=sys.stdin.readline

n=int(input().strip())

arr=[]
for _ in range(n):
    arr.append(int(input().strip()))

arr.sort()
print(mean(arr,n))
print(median(arr,n))
print(mode(arr,n))
print(scope(arr))