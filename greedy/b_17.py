'''
동빈나 그리디 만들수 없는 금액
입력예제 5
3 2 1 1 9 
'''

n=int(input())
arr=list(map(int,input().split()))
arr.sort()

target=1
for x in arr:
    if target<x:
        break
    target+=x
print(target)