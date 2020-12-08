'''
달팽이는 올라가고 싶다 성공출처다국어분류
시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
0.15 초 (추가 시간 없음)	128 MB	70426	16819	14241	25.880%
문제
땅 위에 달팽이가 있다. 이 달팽이는 높이가 V미터인 나무 막대를 올라갈 것이다.

달팽이는 낮에 A미터 올라갈 수 있다. 하지만, 밤에 잠을 자는 동안 B미터 미끄러진다. 또, 정상에 올라간 후에는 미끄러지지 않는다.

달팽이가 나무 막대를 모두 올라가려면, 며칠이 걸리는지 구하는 프로그램을 작성하시오.

입력
첫째 줄에 세 정수 A, B, V가 공백으로 구분되어서 주어진다. (1 ≤ B < A ≤ V ≤ 1,000,000,000)

출력
첫째 줄에 달팽이가 나무 막대를 모두 올라가는데 며칠이 걸리는지 출력한다.
'''

# 1. (a-b)*n+a>=v 를 만족하는 n >= (v-a)/(a-b)
# 2. 하지만 n 은 마지막 a 를 오르기 전 day 이기때문에 
# 마지막 +1 이 필요하다. 따라서, 올림(소수는 x, 소수 마저 오르긴 올라야 하기 때문이다.) + 1 

import sys
import math
input=sys.stdin.readline

a,b,v=map(int,input().strip().split())

print(math.ceil((v-a)/(a-b))+1)