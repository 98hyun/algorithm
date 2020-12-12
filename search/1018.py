'''
체스판 다시 칠하기 성공출처분류
시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
2 초	128 MB	28397	12810	10617	46.354%
문제
지민이는 자신의 저택에서 MN개의 단위 정사각형으로 나누어져 있는 M*N 크기의 보드를 찾았다. 어떤 정사각형은 검은색으로 칠해져 있고, 나머지는 흰색으로 칠해져 있다. 지민이는 이 보드를 잘라서 8*8 크기의 체스판으로 만들려고 한다.

체스판은 검은색과 흰색이 번갈아서 칠해져 있어야 한다. 구체적으로, 각 칸이 검은색과 흰색 중 하나로 색칠되어 있고, 변을 공유하는 두 개의 사각형은 다른 색으로 칠해져 있어야 한다. 따라서 이 정의를 따르면 체스판을 색칠하는 경우는 두 가지뿐이다. 하나는 맨 왼쪽 위 칸이 흰색인 경우, 하나는 검은색인 경우이다.

보드가 체스판처럼 칠해져 있다는 보장이 없어서, 지민이는 8*8 크기의 체스판으로 잘라낸 후에 몇 개의 정사각형을 다시 칠해야겠다고 생각했다. 당연히 8*8 크기는 아무데서나 골라도 된다. 지민이가 다시 칠해야 하는 정사각형의 최소 개수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 N과 M이 주어진다. N과 M은 8보다 크거나 같고, 50보다 작거나 같은 자연수이다. 둘째 줄부터 N개의 줄에는 보드의 각 행의 상태가 주어진다. B는 검은색이며, W는 흰색이다.

출력
첫째 줄에 지민이가 다시 칠해야 하는 정사각형 개수의 최솟값을 출력한다.
'''

# 1. 완전탐색
# 2. 내 기준에 완전히 맞춰놓는 문제다.

n,m=map(int,input().split())
chess=[list(input()) for _ in range(n)]
Min=9999

for a in range(n-7):
    for b in range(m-7):
        count_w=0
        count_b=0
        for i in range(a,a+8):
            for j in range(b,b+8):
                if i%2==0 and j%2==0:
                    if chess[i][j]=='B':
                        count_b+=1
                elif i%2==0 and j%2==1:
                    if chess[i][j]=='W':
                        count_b+=1
                elif i%2==1 and j%2==0:
                    if chess[i][j]=='W':
                        count_b+=1
                elif i%2==1 and j%2==1:
                    if chess[i][j]=='B':
                        count_b+=1
        for i in range(a,a+8):
            for j in range(b,b+8):
                if i%2==0 and j%2==0:
                    if chess[i][j]=='W':
                        count_w+=1
                elif i%2==0 and j%2==1:
                    if chess[i][j]=='B':
                        count_w+=1
                elif i%2==1 and j%2==0:
                    if chess[i][j]=='B':
                        count_w+=1
                elif i%2==1 and j%2==1:
                    if chess[i][j]=='W':
                        count_w+=1
        Min=min(Min,count_b,count_w)
print(Min)



# 다른 풀이

c1 = ['WBWBWBWB','BWBWBWBW']*4
c2 = ['BWBWBWBW','WBWBWBWB']*4

a, b = map(int, input().split())
chess = [input() for _ in range(a)]

min_gap = 64
for i in range(a-7):
    for j in range(b-7):
        gap1, gap2 = 0, 0
        for p in range(8):
            for q in range(8):
                if chess[i+p][j+q]!=c1[p][q]:
                    gap1+=1
                if chess[i+p][j+q]!=c2[p][q]:
                    gap2+=1
        min_gap = min(gap1, gap2, min_gap)

print(min_gap)