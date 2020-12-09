'''
네 번째 점 성공출처다국어분류
시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
1 초	128 MB	12300	8850	8077	73.783%
문제
세 점이 주어졌을 때, 축에 평행한 직사각형을 만들기 위해서 필요한 네 번째 점을 찾는 프로그램을 작성하시오.

입력
세 점의 좌표가 한 줄에 하나씩 주어진다. 좌표는 1보다 크거나 같고, 1000보다 작거나 같은 정수이다.

출력
직사각형의 네 번째 점의 좌표를 출력한다.
'''

# 1. math
# 2. 꼭짓점 수

arr=[]
for _ in range(3):
    arr.append(tuple(map(int,input().split())))
arr.sort(key=lambda x:(x[0],x[1]))

if arr[0][0]==arr[1][0]:
    if arr[1][1]==arr[2][1]:
        print(arr[2][0],arr[0][1])
    else:
        print(arr[2][0],arr[1][1])
else:
    if arr[0][1]==arr[1][1]:
        print(arr[0][0],arr[2][1])
    else:
        print(arr[0][0],arr[1][1])


# 다른 풀이

x=[]
y=[]

for i in range(3):
    a,b=map(int,input().split())
    x.append(a)
    y.append(b)

for i in range(3):
    if x.count(x[i])==1:
        a=x[i]
    if y.count(y[i])==1:
        b=y[i]
print(a,b)