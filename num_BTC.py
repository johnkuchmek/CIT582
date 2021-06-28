import math

def num_BTC(b):
    blocksToCalculate = b
	currentReward = float(50)
	c = float(0)
	while blocksToCalculate != 0:
		if blocksToCalculate % 210000 == 0:
			currentReward = currentReward / 2
			c = c + currentReward
			blocksToCalculate = blocksToCalculate - 1
		else:
			c = c + currentReward
			blocksToCalculate = blocksToCalculate - 1
    return c


