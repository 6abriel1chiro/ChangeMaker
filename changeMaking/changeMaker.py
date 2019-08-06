#greesy method and Dynamic programming
def __coin_matrix__(coinList, changeNum):
    matrix=[[0 for m in range(changeNum+1)]for m in range(len(coinList)+1)]
    for i in range(changeNum+1):
        matrix[0][i]=i
    return matrix

def makeChange(coins,change):
    matrix=__coin_matrix__(coins,change)
    for c in range(1,len(coins)+1):
        for r in range(1,change+1):
            if coins[c-1]==r:
                matrix[c][r]=1
            elif coins[c-1] > r:
                matrix[c][r]=matrix[c-1][r]
            else:
                matrix[c][r] = min(matrix[c-1][r],1+matrix[c][r-coins[c-1]])

    return matrix[-1][-1]

print (makeChange([1,2,5,10,20], 32)) # any list of "coins" ,  any number
