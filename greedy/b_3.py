# 0. 동빈나 책. 1이 될때 까지.
# 1. greedy
# 2. 빼야한다면 빼고, 나눌수있다면 나누기먼저.
# 입력예제 
# 17 4 답은 3

n,k=map(int,input().split())

count=0
while 1:
    temp=(n//k)*k
    count+=n-temp
    n=temp
    if n<k:
        break
    count+=1
    n//=k

count+=n-1
print(count)