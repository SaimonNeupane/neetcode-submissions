class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas)< sum(cost):
            return -1
        else:
            total=0
            temp=0
            res=0
            for i in range(len(gas)):
                total=gas[i]-cost[i]+total
                if total < 0:
                    total=0
                    res=i+1
                    continue
            return res
                