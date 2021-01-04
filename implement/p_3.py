'''
수많은 마라톤 선수들이 마라톤에 참여하였습니다. 단 한 명의 선수를 제외하고는 모든 선수가 마라톤을 완주하였습니다.

마라톤에 참여한 선수들의 이름이 담긴 배열 participant와 완주한 선수들의 이름이 담긴 배열 completion이 주어질 때, 완주하지 못한 선수의 이름을 return 하도록 solution 함수를 작성해주세요.

제한사항
마라톤 경기에 참여한 선수의 수는 1명 이상 100,000명 이하입니다.
completion의 길이는 participant의 길이보다 1 작습니다.
참가자의 이름은 1개 이상 20개 이하의 알파벳 소문자로 이루어져 있습니다.
참가자 중에는 동명이인이 있을 수 있습니다.

입력 예제 : list
출력 예제 : str

participant=['marina','josipa', 'nikola', 'vinko', 'filipa']
completion=['josipa', 'filipa', 'marina', 'nikola']

participant=['mislav', 'stanko', 'mislav', 'ana']
completion=['stanko', 'ana', 'mislav']
'''

# 1. 자료구조 dictionary 
# 2. 다른 풀이에는 collections 의 Counter를 사용하는 경우도 있다. (덧셈,뺄셈이 가능해서)
# 3. 그리고 hash 라는 내장함수를 사용하여 푸는 경우도 있다. 

participant=['mislav', 'stanko', 'mislav', 'ana']
completion=['stanko', 'ana', 'mislav']

def solution(participant,completion):
    people=dict()
    for p in participant:
        if p in people:
            people[p]+=1
        else:
            people[p]=1
    for c in completion:
        if people[c]==1:
            del people[c]
        else:
            people[c]-=1
    return list(people.keys())[0]

print(solution(participant,completion))


# hash는 문자열을 hash 숫자로 바꿔준다.
# 이번 문제에서는 무조건 1명만 완주를 못하기때문에 hash를 통한 뺄셈이 가능했다.

def solution(participant, completion):
    answer = ''
    temp = 0
    dic = {}
    for part in participant:
        dic[hash(part)] = part
        temp += int(hash(part))
    for com in completion:
        temp -= hash(com)
    answer = dic[temp]

    return answer