# 과일장수

def solution(k, m, score):
    answer = 0
    box = len(score) // m
    for i in range(box):
        for j in range(m):
            if j == m - 1 :
                answer += max(score) * m 
            score.pop(score.index(max(score)))
    return answer
    
# --------------------------------------------------------------------------
        

def solution(k, m, score):
    answer = 0 
    score.sort(reverse=True)
    if len(score) >= m:
        for i in range(0, len(score) , m) :
                if len(score[i:i+m]) == m :
                    answer += min(score[i:i+m]) * m
    return answer
    
# 상자의 갯수 len(score) / m 를 구하고 
# 반복문을 이용하여 박스를 만들고 max를 이용해서 최대값을 먼저 추출한다음 마지막으로 박스에 들어가는 숫자 * 개수(k)
# 이익을 명시하면 완료이다  -> 정답은 완료되었지만 중복 for문의 사용으로 점수가 낮게 나와 다시 문제를 풀 필요를 느꼈다.
# for문을 이용해서 매개인자를 3개이용하여 sort된 배열을 가지고 추출하였다. 내부에 if문을 삽입하여 나머지로 생성된 박스에서는
# 값을 더하지 않도록 설정하는 작업을 수행하도록 코드를 작성하였다.


def solution(k, m, score):
    return sum(sorted(score)[len(score)%m::m])*m
    
# - 좋은 풀이의 예시 
