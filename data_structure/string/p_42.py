# 왜 이건 안되는지
# def cleanText(text):
#     text=re.sub('[~!@#$%^&*()=+[{]}:?,<>/]','',text)
#     return text

# https://programmers.co.kr/learn/courses/30/lessons/72410

import re

# def cleanText(text):
#     text=re.sub('[=+,#/\?:^$@*\"※~&%ㆍ!』\\‘|\(\)\[\]\<\>`\'…》]','',text)
#     return text

# def stage_6(text):
#     if text[0]=='.':
#         text=text[1:]
#     if text[-1]=='.':
#         text=text[:-1]
#     return text

# def solution(new_id):
#     new_id=new_id.lower()
#     new_id=cleanText(new_id)
#     n=len(new_id)
#     res=new_id[0]
#     for i in range(1,n):
#         if res[-1]!=new_id[i]:
#             res+=new_id[i]
#     if res[0]=='.':
#         res=res[1:]
#     if res[-1]=='.':
#         res=res[:-1]
#     if res=='':
#         res+='a'
#     n=len(res)
#     if n>=16:
#         res=res[:15]
#     if n<=2:
#         res+=(3-n)*res[-1]
#     res=stage_6(res)
#     return res

# print(solution('.1.'))


import re

def solution(new_id):
    answer = ''
    # 1단계 & 2단계 : 소문자 치환
    answer = re.sub('[^a-z\d\-\_\.]', '', new_id.lower())
    # 3단계 : 마침표 2번 이상 > 하나로
    answer = re.sub('\.\.+', '.', answer)
    # 4단계 : 양 끝 마침표 제거
    answer = re.sub('^\.|\.$', '', answer)
    # 5단계 : 빈 문자열이면 a 대입
    if answer == '':
        answer = 'a'
    # 6단계 : 길이가 16자 이상이면 1~15자만 남기기 & 맨 끝 마침표 제거
    answer = re.sub('\.$', '', answer[0:15])
    # 7단계 : 길이가 3이 될 때까지 반복해서 끝에 붙이기
    while len(answer) < 3:
        answer += answer[-1:]
    return answer
    
print(solution('.1.'))
