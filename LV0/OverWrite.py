# 문자열 overwirte 


def solution(my_string, overwrite_string, s):
    for i in range(s,len(my_string)):
        if i - s < len(overwrite_string) :
            my_string = my_string[:i] + overwrite_string[i-s] + my_string[i+1:]
    return my_string

# -> 내가 푼 답변 

def solution(my_string, overwrite_string, s):
    answer = my_string[:s] + overwrite_string + my_string[len(overwrite_string):]

# -> 다른 사람의 답변