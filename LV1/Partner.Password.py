'''
두 문자열 s와 skip, 그리고 자연수 index가 주어질 때, 다음 규칙에 따라 문자열을 만들려 합니다. 암호의 규칙은 다음과 같습니다.

문자열 s의 각 알파벳을 index만큼 뒤의 알파벳으로 바꿔줍니다.
index만큼의 뒤의 알파벳이 z를 넘어갈 경우 다시 a로 돌아갑니다.
skip에 있는 알파벳은 제외하고 건너뜁니다.
예를 들어 s = "aukks", skip = "wbqd", index = 5일 때, a에서 5만큼 뒤에 있는 알파벳은 f지만 [b, c, d, e, f]에서 'b'와 'd'는 skip에 포함되므로 세지 않습니다. 따라서 'b', 'd'를 제외하고 'a'에서 5만큼 뒤에 있는 알파벳은 [c, e, f, g, h] 순서에 의해 'h'가 됩니다. 나머지 "ukks" 또한 위 규칙대로 바꾸면 "appy"가 되며 결과는 "happy"가 됩니다.

두 문자열 s와 skip, 그리고 자연수 index가 매개변수로 주어질 때 위 규칙대로 s를 변환한 결과를 return하도록 solution 함수를 완성해주세요.
'''

'''
s	        skip	index	result
"aukks" 	"wbqd"	5	    "happy"
''' 

# 문자열에 존재하는 문자를 강제적으로 바꿔치기 하려고했는데 string은 immutable 타입으로 수정이 불가능하다는 것을 간과하고 있었다.
# 'str' object does not support item assignment 에러가 발생하였다. replace를이용해서 이를 해결하고자 하였다.
#  replace('변하기 전 문자열' , '변한 이후의 문자열' , 인자 )
#  인덱스를 추가해줄건데 만약 인덱스를 추가한 상태에서 skip을 만난다면 한 번 더 작동하도록 하고 그게 아니라면 정상작동하도록 만든다
# skip에 해당하는 것들의 ascil코드를 구하고 , s에 속하는 문자들의 ascil 코드를 구해서 이를해결한다 .
# ord와 chr을 사용해서 값을 구할 수 있다. 

# 현재 하려는 작업은 문자열을 chr단위로 분리하고 분리된 단위에서 숫자로 변환된 이후에 5를 더하는 반복문을 돌릴 것이다. 
# 하지만 더 하는 경우에 pass의 숫자에 포함될경우 pass_count의 숫자를세어서 최종적인 숫자를 추가하는 방식으로 정한다.

# 1.skip을 숫자로 변환하는 for 반복문 생성하기.
# [119, 98, 113, 100]
# 2.주어진 문자열에 odr로 구해서 더한이후의 skip_list에 속한다면 +1을 더하도록 설정해두기.
# 3.예외사항으로 123이 넘는경우에는 다시 97로 반환되도록 설정을 해두었다.
# 정답은 맞았지만 체점에서 다른 오류가 있는것으로 화인되어 넘어가지 못하고 있는상태임

s = "aukks"
skip =	"wbqd"	
index = 5

def solution(s, skip, index):
    result = ''

    for j in range(len(s)):
        num = ord(s[j])
        count = 0
        for p in range(len(skip)):
            if num < ord(skip[p]) <= num + index : 
                count += 1

        if num + count + index >= 123:
            result += chr(num + count + index - 26 )  
        else :
            result += chr(num + count + index) 
    return result

def solution(s, skip, index):
    answer = ''
    
    for c in s:
        i = ord(c)
        j = index
        while j > 0:
            i += 1
            if i > ord('z'):
                i = ord('a')
            if chr(i) in skip:
                j += 1
            j -= 1
        answer += chr(i)
    
    return answer

# 다른 사람의 풀이
# ord를 이용해서 간단하게 이를 해결하였고 while문의 사용으로 index의 수를 이용해서 이를 간단하게 해결하였다.

def solution(s, skip, index):
    answer = ''

    for c in s:
        i = ord(c)
        j = index
        while j > 0:
            i += 1
            if i > ord('z'):
                i = ord('a')
            if chr(i) in skip:
                j += 1
            j -= 1
        answer += chr(i)    
    return answer 

print(solution(s, skip, index))