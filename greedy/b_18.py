'''
동빈나 그리디 볼링공
입력예제
5 3
1 3 2 3 2
답 8
'''

n,m=map(int,input().split())
arr=list(map(int,input().split()))

count=0
for i in range(n-1):
    for j in range(i+1,n):
        if arr[i]!=arr[j]:
            count+=1
print(count)

# 답

n,m=map(int,input().split())
arr=list(map(int,input().split()))

dp=[0]*11
for x in arr:
    dp[x]+=1

result=0
for i in range(1,m+1):
    n-=arr[i]
    result+=arr[i]*n
print(result)