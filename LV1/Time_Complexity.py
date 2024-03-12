
def getMyDivisor(n):

    divisorsList = []

    for i in range(1, int(n**(1/2)) + 1):
        if (n % i == 0):
            divisorsList.append(i) 
            if ( (i**2) != n) : 
                divisorsList.append(n // i)

    divisorsList.sort()
    
    return divisorsList
    
    
    # - M x N 이라는 식을 이용해서 이를 해결하였다.  
    # 기존의 시간복잡도가 O(n)이라는 점에서 -> O(1/2)로 변경되었다.
    # 약수구하기를 시간복잡도를 이용해서 쉽게 해결할 수 있었다.

    
    # -------------------------------------------------------------------------
    
    


