# 0. 동빈나 책. 숫자카드게임.
# 1. greedy
# 2. 각 행마다 가장 작은수를 찾은 뒤에 그 중 큰수를 출력.
# 입력예제 
# 2 4
# 7 3 1 8
# 3 3 3 4 답은 3
m,n=map(int,input().split())

arr=[]
for i in range(m):
    arr.append(list(map(int,input().split())))

temp=[]
for i in range(m):
    temp.append(min(arr[i]))
print(max(temp))

# 정답

m,n=map(int,input().split())
temp=0

for i in range(m):
    arr=list(map(int,input().split()))
    v=min(arr)
    temp=max(result,v)
print(temp)