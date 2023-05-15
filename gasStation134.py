from collections import deque
class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        carriedOver = 0
        greedyGas = (gas[0] - cost[0])
        index = 0
        for i in range(1, len(gas)):
            nex = gas[i] - cost[i]
            if greedyGas < 0:
                carriedOver += greedyGas
                greedyGas = nex
                index = i 
            else:
                greedyGas += nex
        if greedyGas < 0 or (greedyGas == 0 and index != 0) or carriedOver + greedyGas < 0:
            return -1
        else:
            return index
