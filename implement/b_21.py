'''
동빈나 문자열 재정렬 문자열끼리 & 합
입력예제 k1ka5cb7 
답 abckk13
'''

s=input()

n=0
arr=[]
for i in s:
    if i.isdigit():
        n+=int(i)
    else:
        arr.append(i)
arr.sort()
print(''.join(arr)+str(n))