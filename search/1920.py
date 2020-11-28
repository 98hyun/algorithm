'''
수 찾기 성공분류
시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
2 초	128 MB	67182	20174	13180	29.760%
문제
N개의 정수 A[1], A[2], …, A[N]이 주어져 있을 때, 이 안에 X라는 정수가 존재하는지 알아내는 프로그램을 작성하시오.

입력
첫째 줄에 자연수 N(1≤N≤100,000)이 주어진다. 다음 줄에는 N개의 정수 A[1], A[2], …, A[N]이 주어진다. 다음 줄에는 M(1≤M≤100,000)이 주어진다. 다음 줄에는 M개의 수들이 주어지는데, 이 수들이 A안에 존재하는지 알아내면 된다. 모든 정수의 범위는 -231 보다 크거나 같고 231보다 작다.

출력
M개의 줄에 답을 출력한다. 존재하면 1을, 존재하지 않으면 0을 출력한다.
'''

# 1. sequence 객체의 in 은 순차탐색 느리다.
# 2. 이분탐색을 활용.

import sys
input=sys.stdin.readline

n=int(input().strip())
arr=list(map(int,input().strip().split()))
arr.sort()
m=int(input().strip())
arr2=list(map(int,input().strip().split()))

start,end=0,n-1
mid=(start+end)//2
for a in arr2:
    start,end=0,n-1
    mid=(start+end)//2
    while end>=start:
        if arr[mid]==a:
            print(1)
            break
        elif arr[mid]>a:
            end=mid-1
        else:
            start=mid+1
        mid=(start+end)//2
    if end<start:
        print(0)
     
