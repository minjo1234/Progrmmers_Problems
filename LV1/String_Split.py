'''
문자열 s가 주어졌을 때, s의 각 위치마다 자신보다 앞에 나왔으면서, 자신과 가장 가까운 곳에 있는 같은 글자가 어디 있는지 알고 싶습니다.
예를 들어, s="banana"라고 할 때,  각 글자들을 왼쪽부터 오른쪽으로 읽어 나가면서 다음과 같이 진행할 수 있습니다.

b는 처음 나왔기 때문에 자신의 앞에 같은 글자가 없습니다. 이는 -1로 표현합니다.
a는 처음 나왔기 때문에 자신의 앞에 같은 글자가 없습니다. 이는 -1로 표현합니다.
n은 처음 나왔기 때문에 자신의 앞에 같은 글자가 없습니다. 이는 -1로 표현합니다.
a는 자신보다 두 칸 앞에 a가 있습니다. 이는 2로 표현합니다.
n도 자신보다 두 칸 앞에 n이 있습니다. 이는 2로 표현합니다.
a는 자신보다 두 칸, 네 칸 앞에 a가 있습니다. 이 중 가까운 것은 두 칸 앞이고, 이는 2로 표현합니다.
따라서 최종 결과물은 [-1, -1, -1, 2, 2, 2]가 됩니다.

문자열 s이 주어질 때, 위와 같이 정의된 연산을 수행하는 함수 solution을 완성해주세요.
'''

'''
s	result
"banana"	[-1, -1, -1, 2, 2, 2]
"foobar"	[-1, -1, 1, -1, -1, -1]
'''

# 배열을 먼저 이용해서 해보려고 하다가 빈 문자열을 이용하면 더욱 더 간단하게 코드를 작성할 수 있음으로 문자열을 이용하였다.
# rfind로 인해서 포함되지 않는경우는 바로 -1을 넣고 -1이 아닐경우에 반복문의 숫자와 rfind의 숫자를 비교해서 추가한다.

def solution(str):
    result = []
    empty_str  = ""
    for i in range(len(str)):
        if empty_str.find(str[i]) == -1:
            result.append(-1) 
            empty_str += str[i]
        elif empty_str.find(str[i]) != -1:
            result.append(i-empty_str.rfind(str[i]))
            empty_str += str[i]
    return result

# 다른 사람의 문제 풀이
# dictionary를 이용해서 간단하게 이를 해결하였다.

def solution(s):
    answer = []
    dic = dict()
    for i in range(len(s)):
        if s[i] not in dic:
            answer.append(-1)
        else:
            answer.append(i - dic[s[i]])
        dic[s[i]] = i

    return answer
