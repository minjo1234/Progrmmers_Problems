'''
햄버거 가게에서 일을 하는 상수는 햄버거를 포장하는 일을 합니다. 함께 일을 하는 다른 직원들이 햄버거에 들어갈 재료를 조리해 주면 조리된 순서대로 상수의 앞에 아래서부터 위로 쌓이게 되고, 상수는 순서에 맞게 쌓여서 완성된 햄버거를 따로 옮겨 포장을 하게 됩니다. 상수가 일하는 가게는 정해진 순서(아래서부터, 빵 – 야채 – 고기 - 빵)로 쌓인 햄버거만 포장을 합니다. 상수는 손이 굉장히 빠르기 때문에 상수가 포장하는 동안 속 재료가 추가적으로 들어오는 일은 없으며, 재료의 높이는 무시하여 재료가 높이 쌓여서 일이 힘들어지는 경우는 없습니다.

예를 들어, 상수의 앞에 쌓이는 재료의 순서가 [야채, 빵, 빵, 야채, 고기, 빵, 야채, 고기, 빵]일 때, 상수는 여섯 번째 재료가 쌓였을 때, 세 번째 재료부터 여섯 번째 재료를 이용하여 햄버거를 포장하고, 아홉 번째 재료가 쌓였을 때, 두 번째 재료와 일곱 번째 재료부터 아홉 번째 재료를 이용하여 햄버거를 포장합니다. 즉, 2개의 햄버거를 포장하게 됩니다.

상수에게 전해지는 재료의 정보를 나타내는 정수 배열 ingredient가 주어졌을 때, 상수가 포장하는 햄버거의 개수를 return 하도록 solution 함수를 완성하시오.

ingredient	result
[2, 1, 1, 2, 3, 1, 2, 3, 1]	2
[1, 3, 2, 1, 2, 1, 3, 1, 2]	0
'''
ingredient = [2, 1, 1, 2, 3, 1, 2, 3, 1]

def solution(ingredient):
    i=0
    answer = 0
    while i < len(ingredient) - 2 :
            if ingredient[i:i+4] == [1, 2, 3, 1] :
                del ingredient[i:i+4] 
                i = 0 
                answer += 1 
                continue    
            i += 1 
    return answer

#  다르 사람의 풀이

def solution(ingredient):
    s = []
    cnt = 0
    for i in ingredient:
        s.append(i)
        print(s[-4:])
        if s[-4:] == [1, 2, 3, 1]:
            cnt += 1
            del s[-4:]
            
    return cnt



# 1231순서로 진행되어야하고 중간에 새로운 숫자가 생기면 진행되지 못한다.
# 햄버거가 완성될경우 해당 인덱스는 제거된다.
# 답은 맞았으나 시간 초과로 인해서 정답을 인식하지 못하였고 비슷한 사례를 검색하여 찾아내었다.
# 인덱스의 잦은 비교와 len의 사용을 최소화했고 pop과 del을 사용하는 방식 중 풀이자는 반복문을 이용한 pop을 사용했지만 
# 나는 del을 사용하여 한 번에 해결하고자 하였다.
