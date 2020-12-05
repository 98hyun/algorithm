'''
벌집 성공출처분류
시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
2 초	128 MB	48524	22225	19355	46.110%
문제


위의 그림과 같이 육각형으로 이루어진 벌집이 있다. 그림에서 보는 바와 같이 중앙의 방 1부터 시작해서 이웃하는 방에 돌아가면서 1씩 증가하는 번호를 주소로 매길 수 있다. 숫자 N이 주어졌을 때, 벌집의 중앙 1에서 N번 방까지 최소 개수의 방을 지나서 갈 때 몇 개의 방을 지나가는지(시작과 끝을 포함하여)를 계산하는 프로그램을 작성하시오. 예를 들면, 13까지는 3개, 58까지는 5개를 지난다.

입력
첫째 줄에 N(1 ≤ N ≤ 1,000,000,000)이 주어진다.

출력
입력으로 주어진 방까지 최소 개수의 방을 지나서 갈 때 몇 개의 방을 지나는지 출력한다.
'''

# 1. math
# 2. 어렵게 생각할 거 없었다. 등차수열
# 규칙을 찾고 +,- 등 간단한 사칙연산 및 반복문을 사용했다.

import sys
input=sys.stdin.readline

n=int(input().strip())

count=1
cnt6=6
cnt=1

while n>cnt:
    count+=1
    cnt+=cnt6
    cnt6+=6
print(count)
    