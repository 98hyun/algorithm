'''
동빈나 그리디 문자열 뒤집기
입력예제
0001100 답 1
'''

s=input()

count0=0
count1=0

# 0으로 만들기
if s[0]=='1':
    count0+=1
# 1로 만들기
else:
    count1+=1

for i in range(len(s)-1):
    if s[i]!=s[i+1]:
        if s[i+1]=='1':
            count0+=1
        else:
            count1+=1
print(min(count0,count1))