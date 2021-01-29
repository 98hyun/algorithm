# 0. 동빈나 책. 큰수의 법칙.
# 1. greedy
# 2. 제일큰수를 k번까지 더하기. 그리고 두번째로 큰수를 더하기. 이걸 m번 까지.
# 입력예제 
# 5 8 3
# 2 4 5 4 6 결과는 46

n,m,k=map(int,input().split())
arr=list(map(int,input().split()))

arr.sort()
temp=0
for i in range(1,m+1):
    if i%k==0:
        temp+=arr[-2]
        continue
    temp+=arr[-1]
print(temp)    