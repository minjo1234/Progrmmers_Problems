# 카드뭉치 

def solution(cards1, cards2, goal):
    answer = 'Yes'
    for value in goal:
            if cards1 !=[] and cards1[0] == value:
                del cards1[0]
                continue
            if cards2 != [] and cards2[0] == value:
                del cards2[0]
                continue
            else :
                answer = 'No'
            break
    return answer
    
# --------------------------------------------------------------------------
    

# 반복문을 이용해서 goal의 요소가 두 개의 배열의 첫 번째 인자에 하나라도 해당한다면 continue 그게 아니라면 answer에 'No'가 인식되도록한다.  - 기본설정을 Yes로 설정하고 , 만약 존재하지 않는다면 No라고 변경되도록 코드를 설정한다.
# 첫 번째 인자에 속한다면 해당 리스트의 첫 번째 인자를 제거해서 사용한다. - del cards[0]
# 제거하는 도중에 빈 배열이 생겨 if문에 오류가 발생하였다 - and 절을 이용해서 이를 해결하였다.
    