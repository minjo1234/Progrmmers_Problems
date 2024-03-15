'''
두 정수 X, Y의 임의의 자리에서 공통으로 나타나는 정수 k(0 ≤ k ≤ 9)들을 이용하여 만들 수 있는 가장 큰 정수를 두 수의 짝꿍이라 합니다(단, 공통으로 나타나는 정수 중 서로 짝지을 수 있는 숫자만 사용합니다). X, Y의 짝꿍이 존재하지 않으면, 짝꿍은 -1입니다. X, Y의 짝꿍이 0으로만 구성되어 있다면, 짝꿍은 0입니다.

예를 들어, X = 3403이고 Y = 13203이라면, X와 Y의 짝꿍은 X와 Y에서 공통으로 나타나는 3, 0, 3으로 만들 수 있는 가장 큰 정수인 330입니다. 다른 예시로 X = 5525이고 Y = 1255이면 X와 Y의 짝꿍은 X와 Y에서 공통으로 나타나는 2, 5, 5로 만들 수 있는 가장 큰 정수인 552입니다(X에는 5가 3개, Y에는 5가 2개 나타나므로 남는 5 한 개는 짝 지을 수 없습니다.)
두 정수 X, Y가 주어졌을 때, X, Y의 짝꿍을 return하는 solution 함수를 완성해주세요.
'''

'''
X	Y	result
"100"	"2345"	"-1"
"166"	"263645"	"0"
"100"	"123450"	"10"
"12321"	"42531"	"321"
"5525"	"1255"	"552"
'''

# for 중복 반복문을 이용하여 일치하는 숫자가 존재한다면 제거해서 새로운 배열에 추가하고 추가된 배열에서 새롭게 추가된 배열에서 
# max를 이용해서 값을 변경하는 식으로 진행했습니다.
# 하지만 문자열을 수정하는 부분에서 오류가 발생하였고 del 사용불가 (문자열을 리스트로 만들거나 , replace를 사용하는 방법이 존재함 
# )
X = "166"
Y = "263645"

def solution(X, Y):
    answer = [] 
    result = ''


def solution(X, Y):
    answer = ''

    for i in range(len(X)):
        for j in range(len(Y)):
            if X[i] == Y[j]:
                answer += (Y[j])
                Y = Y.replace(Y[j], "" , 1)
                break  
    if answer == '' or answer == "":
        answer = '-1'
    else : 
        answer = ''.join(sorted(answer, reverse=True))
        answer = str(int(answer)) 

    return answer



# 문제해결방식으로는 중복 반복문을 통해서 인덱스가 일치한다면 제거하는 방식으로 진행한다.
# 또한 문자열과 정수형 과정에서 if ~ elif 구문을적용하여 문제를 해결하였고 모두 정답을 맞추었다.
# 하지만 시간초과가 발생하였다. 시간초과가 발생한 이후에 코드를 수정하여 sorted를 이용하여 간단하게 해결하였지만 또 시간초과가 발생하였다.
# 그래서 dictionary 형태로 정렬이 가능한 Counter 모듈을 사용하기로 하였다. 

from collections import Counter

def solution(X, Y):
    # 숫자 개수 세기
    # Counter를 사용하면 dictionary 형태로 숫자를 받을 수 있다.
    nums = Counter(X) & Counter(Y) 
    
    if not nums : return '-1' # 공통이 없는 경우 
    elif list(nums) == ['0'] : return 0 

    nums_order = sorted(list(nums),reverse=True) # 내림차순 정렬
    answer = ''
    for num in nums_order:
        answer += num * nums[num]
    return answer


# Counter 모듈을 사용하여 dictionary 형태로 저장하고 저장된 형태로 공통이 없는 경우 , 공통이 0만 존재하는 경우 
# 마지막으로 다양한 공통이 존재하는 경우에는 sort를 실행한 이후 dictionary의 key:item으로 곱해서 최대정수를 구하는 방식으로 진행하였다.
# for 문을 이용한 다른 풀이도 존재하지만 Collection 모듈을 사용하는게 시간복잡도가 O(n)으로 최소값이기에 사용하기에 가장 간편하고 좋다.


