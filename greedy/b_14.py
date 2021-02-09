# 동빈나 그리디 모험가 길드
# 공포도가 x 인 모험가는 x명 이상의 그룹에 들어가야한다. -> 최대 몇 그룹
# 1. 정렬 후 끊기
# 입력 예제 
# 5
# 2 3 2 2 1 답 2

n=int(input())

arr=list(map(int,input().split()))
arr.sort()

team=0
count=0
for i in arr:
    count+=1
    if count>=i:
        team+=1
        count=0
print(team)