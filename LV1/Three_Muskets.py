'''
한국중학교에 다니는 학생들은 각자 정수 번호를 갖고 있습니다. 이 학교 학생 3명의 정수 번호를 더했을 때 0이 되면 3명의 학생은 삼총사라고 합니다. 예를 들어, 5명의 학생이 있고, 각각의 정수 번호가 순서대로 -2, 3, 0, 2, -5일 때, 첫 번째, 세 번째, 네 번째 학생의 정수 번호를 더하면 0이므로 세 학생은 삼총사입니다. 또한, 두 번째, 네 번째, 다섯 번째 학생의 정수 번호를 더해도 0이므로 세 학생도 삼총사입니다. 따라서 이 경우 한국중학교에서는 두 가지 방법으로 삼총사를 만들 수 있습니다.

한국중학교 학생들의 번호를 나타내는 정수 배열 number가 매개변수로 주어질 때, 학생들 중 삼총사를 만들 수 있는 방법의 수를 return 하도록 solution 함수를 완성하세요.
'''

'''
number	result
[-2, 3, 0, 2, -5]	2
[-3, -2, -1, 0, 1, 2, 3]	5
[-1, 1, -1, 1]	0
'''

# 삼총사의 갯수 만들기
# 인덱스 순으로 (012 , 013 , 014 , 023 , 024 , 034 , 123 , 124 , 134  , 234)
# 5C3라는 가정하에 permuttions를 사용하지 않고 , combinations를 사용하려고 하였다.
# 라이브러리가 존재해서 해당 라이브러리를 사용하려고 한다. -> from itertools
# permutations는 순서를 고려하고 , combinations는 순서를 고려하지 않는다 -> 확률과 동계에서 P , C를 생각하면 쉽다.

from itertools import permutations, combinations

fruits_li=['사과', '배', '바나나']
bread_li=['식빵', '소보루빵', '크림빵']
drink_li=['주스', '맥주', '요거트']


# 각 리스트에서 N개만큼 뽑아 나열할 경우(순서 고려)
per_fruits=list(permutations(fruits_li, 2)) # N=2
# print(per_fruits)

# 각 리스트 나열 시 N개만큼 뽑아 나열할 경우 출력(순서 고려하지 않음)
fruits_con=list(combinations(fruits_li, 2)) # N=2
# print(fruits_con)

number = [-2, 3, 0, 2, -5]

zero_number = list(combinations(number, 3))


def solution(number):
    answer = 0
    zero_number = list(combinations(number, 3))     
    for i in range(0, len(zero_number)):
        if sum(zero_number[i]) == 0 :
            answer += 1
    return answer

# 다른 사람의 풀이 
# 직관적으로 i , j , k를 이용해서 서로의 범위를 나눈다면 모듈을 사용하지 않고도 이 문제의 해결이 가능하다.

def solution(number):
    answer = 0
    l = len(number)
    for i in range(l-2):
        for j in range(i+1, l-1):
            for k in range(j+1, l):
                # print(number[i],number[j],number[k])
                if number[i]+number[j]+number[k] == 0:
                    answer += 1           
    return answer

