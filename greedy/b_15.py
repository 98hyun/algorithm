# 동빈나 그리디 곱하기 더하기
# 숫자 문자열. 사이사이에 x 혹은 +로 큰 수 
# 1. 곱하거나 더할 수 혹은 계산중인 수가 <= 1 일때 더한다.
# 입력 예제 
# 02984 답 576

s=input().strip()

temp=0
for i in s:
    if i=='0' or i=='1':
        temp+=int(i)
    else:
        if temp==0:
            temp=1
        temp*=int(i)
print(temp)

# 답 

s=input()

temp=int(s[0])
for i in s[1:]:
    n=int(i)
    if n<=1 or temp<=1:
        temp+=n
    else:
        temp*=n
print(temp)