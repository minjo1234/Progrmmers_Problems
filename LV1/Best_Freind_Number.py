'''
두 정수 X, Y의 임의의 자리에서 공통으로 나타나는 정수 k(0 ≤ k ≤ 9)들을 이용하여 만들 수 있는 가장 큰 정수를 두 수의 짝꿍이라 합니다(단, 공통으로 나타나는 정수 중 서로 짝지을 수 있는 숫자만 사용합니다). X, Y의 짝꿍이 존재하지 않으면, 짝꿍은 -1입니다. X, Y의 짝꿍이 0으로만 구성되어 있다면, 짝꿍은 0입니다.

예를 들어, X = 3403이고 Y = 13203이라면, X와 Y의 짝꿍은 X와 Y에서 공통으로 나타나는 3, 0, 3으로 만들 수 있는 가장 큰 정수인 330입니다. 다른 예시로 X = 5525이고 Y = 1255이면 X와 Y의 짝꿍은 X와 Y에서 공통으로 나타나는 2, 5, 5로 만들 수 있는 가장 큰 정수인 552입니다(X에는 5가 3개, Y에는 5가 2개 나타나므로 남는 5 한 개는 짝 지을 수 없습니다.)
두 정수 X, Y가 주어졌을 때, X, Y의 짝꿍을 return하는 solution 함수를 완성해주세요.
'''

'''
X	Y	result
"100"	"2345"	"-1"
"100"	"203045"	"0"
"100"	"123450"	"10"
"12321"	"42531"	"321"
"5525"	"1255"	"552"
'''

# for 중복 반복문을 이용하여 일치하는 숫자가 존재한다면 제거해서 새로운 배열에 추가하고 추가된 배열에서 새롭게 추가된 배열에서 
# max를 이용해서 값을 변경하는 식으로 진행했습니다.
# 하지만 문자열을 수정하는 부분에서 오류가 발생하였고 del 사용불가 (문자열을 리스트로 만들거나 , replace를 사용하는 방법이 존재함 
# )
X = "100"
Y = "2345"

def solution(X, Y):
    answer = [] 
    result = ''

    for i in range(len(X)):
        for j in range(len(Y)):
            if X[i] == Y[j]:
                answer.append(Y[j])
                Y = Y.replace(Y[j], "" , 1)
                break  
    print(answer)

    if answer == [] :
        result = '-1' 
    elif max(answer) == '0' :
        result = '0' 
    else :
        for p in range(len(answer)):
            result += max(answer)
            del answer[answer.index(max(answer))]
   
    return result


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


print(solution(X, Y)) 

# 문제해결방식으로는 중복 반복문을 통해서 인덱스가 일치한다면 제거하는 방식으로 진행한다.
# 또한 문자열과 정수형 과정에서 if ~ elif 구문을적용하여 문제를 해결하였고 모두 정답을 맞추었다.
# 하지만 시간초과가 발생하였다.
