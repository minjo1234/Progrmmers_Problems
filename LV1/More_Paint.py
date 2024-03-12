# 덧칠하기

def solution(n, m, section):
    answer = 0
    for i in range(len(section)):
        if i == len(section) -1 :
            answer += 1
            break
        for j in range(i+1,len(section)):
            if section[i] + m -1 >= section[j] :
                continue
            else :
                i = j
                answer += 1
                break

    answer <= n / m
    return answer
    
#  ------------------------------------------------------------------------------
 
 
def solution(n,m,section):
    answer = 0
    paint = 0

    for value in section:
        if(value > paint):
            paint = value + m - 1
            answer += 1
    return answer
    
    
# 내가 하려던 방식은 패인트를 칠하는 for 반복문을 사용했는데 
# section의 비교를 통해서 이미 칠해져있다면 넘기고 , 칠해져있지않다면 다음영역으로 넘어가면서 count를 활용해주자고 생각하였는데
# 반복문 , continue , break의 다중사용으로 인해 오류가 발생하고 말았다.
# 그래서 중복 for문을 제거하고 패인트를 칠한다음에 그 영역이후에 숫자가 나온다면 다시 칠하는 방식으로 진행하고자 한다.