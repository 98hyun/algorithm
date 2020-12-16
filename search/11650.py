'''
좌표 정렬하기 성공분류
시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
1 초	256 MB	34260	16437	12571	48.759%
문제
2차원 평면 위의 점 N개가 주어진다. 좌표를 x좌표가 증가하는 순으로, x좌표가 같으면 y좌표가 증가하는 순서로 정렬한 다음 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 점의 개수 N (1 ≤ N ≤ 100,000)이 주어진다. 둘째 줄부터 N개의 줄에는 i번점의 위치 xi와 yi가 주어진다. (-100,000 ≤ xi, yi ≤ 100,000) 좌표는 항상 정수이고, 위치가 같은 두 점은 없다.

출력
첫째 줄부터 N개의 줄에 점을 정렬한 결과를 출력한다.
'''

# 1. 정렬
# 2. 좌표 같이 짝꿍인 것은 같이 움직여야한다. 
# 처음엔 x,y 나눠서 했는데 말이 안됐다.

n=int(input())
array=[]

for _ in range(n):
    a,b=map(int,input().split(' '))
    array.append((a,b))
array=sorted(array,key=lambda x:(x[0],x[1]))

for i,j in array:
    print(i,j)
