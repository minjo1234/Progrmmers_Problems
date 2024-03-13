'''
임의의 양의 정수 n에 대해, n이 어떤 양의 정수 x의 제곱인지 아닌지 판단하려 합니다.
n이 양의 정수 x의 제곱이라면 x+1의 제곱을 리턴하고, n이 양의 정수 x의 제곱이 아니라면 -1을 리턴하는 함수를 완성하세요.

n	return
121	144
3	-1
'''
import math

def solution(n):
    if n == int(math.pow(n**(1/2),2)): 
        answer = int(math.pow((n**(1/2))+1 ,2 )) 
    else :
        answer = -1
    return answer 

#  답은 맞는데 정답은 틀리는거로 나온다. 정답을 확인해보기로함 

def solution(n):
    if int(n**0.5) == n**0.5: #제곱수 판별
        return ((n**0.5)+1)**2 # 제곱근+1의 제곱수 반환
    else : 
        return -1 #제곱수 아니면 -1반환
    
# 제곱근일 경우 int를 추가해도 동일하기에 이를 추가해서 문제를 해결하였다.

