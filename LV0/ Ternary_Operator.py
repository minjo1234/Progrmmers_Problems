# 삼항연산자

# [True일 때의 값] if [조건식] else [False일 때의 값]
# n을 입력받아서 짝수 홀수를 비교하려는 경우에 사용하는 식

n = int(input())
print(f'{n} is', 'odd' if n % 2 else 'even')