import math

def num_BTC(b):
    currentBlock = 0
    currentReward = float(50)
    c = float(0)
    while currentBlock != b:
        if currentBlock % 210000 == 0:
            currentBlock = currentBlock + 1
            currentReward = currentReward / 2
			c = c + currentReward
        else:
            c = c + currentReward
            currentBlock = currentBlock + 1
    return c


