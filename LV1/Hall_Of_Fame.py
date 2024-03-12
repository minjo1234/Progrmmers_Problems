#  명예의 전당

'''
"명예의 전당"이라는 TV 프로그램에서는 매일 1명의 가수가 노래를 부르고, 시청자들의 문자 투표수로 가수에게 점수를 부여합니다. 매일 출연한 가수의 점수가 지금까지 출연 가수들의 점수 중 상위 k번째 이내이면 해당 가수의 점수를 명예의 전당이라는 목록에 올려 기념합니다. 즉 프로그램 시작 이후 초기에 k일까지는 모든 출연 가수의 점수가 명예의 전당에 오르게 됩니다. k일 다음부터는 출연 가수의 점수가 기존의 명예의 전당 목록의 k번째 순위의 가수 점수보다 더 높으면, 출연 가수의 점수가 명예의 전당에 오르게 되고 기존의 k번째 순위의 점수는 명예의 전당에서 내려오게 됩니다.

이 프로그램에서는 매일 "명예의 전당"의 최하위 점수를 발표합니다. 예를 들어, k = 3이고, 7일 동안 진행된 가수의 점수가 [10, 100, 20, 150, 1, 100, 200]이라면, 명예의 전당에서 발표된 점수는 아래의 그림과 같이 [10, 10, 10, 20, 20, 100, 100]입니다.

명예의 전당 목록의 점수의 개수 k, 1일부터 마지막 날까지 출연한 가수들의 점수인 score가 주어졌을 때, 매일 발표된 명예의 전당의 최하위 점수를 return하는 solution 함수를 완성해주세요.
'''


'''
k	score	result
3	[10, 100, 20, 150, 1, 100, 200]	[10, 10, 10, 20, 20, 100, 100]
4	[0, 300, 40, 300, 20, 70, 150, 50, 500, 1000]	[0, 0, 0, 0, 20, 40, 70, 70, 150, 300]
'''

# 명예의 전당중에서 최하위의 점수에 위치하는 것을 찾는 문제로 
# 1.반복문을 이용해서 차례대로 score를 넣을것이고  - for i in range(len(score))
# 2.sort 조건절을 이용해서 리스트에 추가하고 말지를 정해서 출력하면 간단하게 완료가 될 것이라고 생각한다.
# 두 개의 배열에 만들어서 하나의 배열에는 명예의 전당이 생성되도록 유지시키고 , 하나의 배열에는 result를 생성한다.
# 오류가 발생했다. -> k에 값이 추가된이후에 그 이후 조건절이 작동하여 오류가 발생하였으므로 순서를 바꾸고 else 구문을 추가하였다.
# 다른 방법으로는 min을 이용하여 최소값으로 sort를 이용하지 않고 하는 방법이 존재할 것 으로 예상됩니다.

k = 4
score = [0, 300, 40, 300, 20, 70, 150, 50, 500, 1000]


def solution(k, score):
    answer = []
    result = [] 
    for i in range(len(score)):
        if len(answer) >= k and score[i] > answer[0]:
            del answer[0]   
            answer.append(score[i])
            answer.sort()
            result.append(answer[0])
        elif len(answer) < k:
            answer.append(score[i])
            answer.sort()
            result.append(answer[0])
        else :
            result.append(answer[0])
    return result

print(solution(k, score))

# 다른 사람의 풀이 


2
3
4
5
6
7
8
9
10
11
12
13
14
def solution(k, score):

    q = []

    answer = []
    for s in score:

        q.append(s)
        if (len(q) > k):
            q.remove(min(q))
        answer.append(min(q))

    return answer

#  따로 길이보다 작은 경우와 길이보다 큰 경우를 나눌필요가 없었고 최소값을 이용하는 방법도 존재한다.
