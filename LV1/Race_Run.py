# 달리기 경주 

def solution(players, callings):
    answer = players.copy()
    for i in range(len(callings)):

        
        x = answer.index(callings[i]) 
        y = int(answer.index(callings[i])) - 1
        answer[x] , answer[y] = answer[y] , answer[x]
    return answer
    
'''    
 정답은 맞았지만 시간복잡도에 따라서 시간초과 현상이 발생하였으므로 다시 해결할 필요가 존재
.index를 사용할경우 시간복잡도가 O(n)으로 존재하지만
dictionary를 변경하서 사용하였음

in enumerate 
player_dict[key] = value
player_dict[key] = value 
가 출력되는 구조를 판단하였음 
'''

def solution(players, callings):
    player_dict = {player: idx for idx, player in enumerate(players)}
    
    for call in callings:
        print(player_dict[call])
        idx = player_dict[call]
        
        players[idx], players[idx-1] = players[idx-1], players[idx]
        
        player_dict[players[idx]] = idx
        player_dict[players[idx-1]] = idx-1
    
    return players
