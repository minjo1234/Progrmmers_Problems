# 푸드 파이터 대회

food = []

def solution(food):
    msg = '0'
    for i in range(len(food)-1, 0, -1):
        if food[i] < 2:
            continue
        if food[i] % 2 == 0:  
            x = food[i] // 2
            for j in range(0,x):
                msg = str(i) + msg + str(i) 
        else:
            x = (food[i] // 2) 
            for j in range(0,x):
                msg = str(i) + msg + str(i)
    return msg


solution(food)


def solution(food):
    answer = "0"
    for i in range(len(food)-1,0,-1):
        c = int(food[i]/2)
        while c > 0:
            answer = str(i) + answer + str(i)
            c -= 1 
    return answer 
    