# 폰켄몬 : 숫자의 절반 중 종류의 최대값 구하기 ( 중복불가 )


def solution(nums):
	return min(len(set(nums)) , len(nums)//2)


nums = [3, 3, 3, 6,6,6]
print(solution(nums))  # 출력: 2



def solution(nums):
	unique_pokemons = len(nums) // 2 
	max_pokemons = set(nums) 

	return min(unique_pokemons , len(max_pokemons))


print(solution(nums))
