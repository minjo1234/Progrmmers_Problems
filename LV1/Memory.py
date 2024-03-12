
# 추억점수 

def solution(name, yearning, photo):
    answer = []

    for i in range(len(photo)):
        num = 0    
        for j in range(len(photo[i])):
            if photo[i][j] in name :
                num += yearning[name.index(photo[i][j])] 
            if j == len(photo[i]) - 1 :
                answer.append(num)  
    return answer
    
    
#  photo의 길이를 어떻게 측정할 것인지를 정하고 그에 따라서 코드를 작성한다. - 중복 for문 
#  해당텍스트가 name 배열에 존재하는지 확인한다 - photo[i][j] in name 
#  인덱스를 추출해서 점수를 합산한다. yearning[name.index(photo[i][j])]
#  내부 for문의 마지막 인덱스에서 값을 추가하고 초기화를 반복한다. result.append()


name = ["may", "kein", "kain", "radi"]
yearning = [5, 10, 1, 3]
photo = [["may", "kein", "kain", "radi"],["may", "kein", "brin", "deny"], ["kon", "kain", "may", "coni"]]