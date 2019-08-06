#greedy method
def changeMaker(cents):
    coinlist=[25,10,5,1]
    counter=0
    for coin in coinlist:
        while cents >= coin:
            cents=cents-coin
            counter=counter+1

    return counter

print(changeMaker(8)) #any number
