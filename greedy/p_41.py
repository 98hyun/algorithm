'''
큰 수 만들기
문제 설명
어떤 숫자에서 k개의 수를 제거했을 때 얻을 수 있는 가장 큰 숫자를 구하려 합니다.

예를 들어, 숫자 1924에서 수 두 개를 제거하면 [19, 12, 14, 92, 94, 24] 를 만들 수 있습니다. 이 중 가장 큰 숫자는 94 입니다.

문자열 형식으로 숫자 number와 제거할 수의 개수 k가 solution 함수의 매개변수로 주어집니다. number에서 k 개의 수를 제거했을 때 만들 수 있는 수 중 가장 큰 숫자를 문자열 형태로 return 하도록 solution 함수를 완성하세요.

제한 조건
number는 1자리 이상, 1,000,000자리 이하인 숫자입니다.
k는 1 이상 number의 자릿수 미만인 자연수입니다.
입출력 예
number	k	return
1924	2	94
1231234	3	3234
4177252841	4	775841
'''

# 1. greedy 문자열
# 2. 나열 없다. 잘랐을때 가장 큰수. 즉, 가장 큰 수가 앞으로와야한다. 
# 질문. while에 arr 길이가 있다는것을 왜 보장해줘야하는지?
# 답. pop으로 arr에서 다 빼고, pop하면 뺄 것이 없어 에러난다. 그래서 arr로 조건 넣기.

def solution(number,k):
    arr=[number[0]]
    for num in number[1:]:
        while arr and num>arr[-1] and k>0:
            arr.pop()
            k-=1
        arr.append(num)
    arr=number[:-k] if k>0 else arr
    return ''.join(arr)

print(solution('99991',3))