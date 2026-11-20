class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        '''my naive soln after trial and error witout rigorous verification
        '''
        # if len(gas) == len(cost) == 1 and gas[0] >= cost[0]:
        #     return 0
             
        # maxTank, maxTankIdx = 0, -1
        # n = len(gas)

        # # find index
        # # tank, cur = 0, 0
        # # for i in range(n):
        # #     if gas[i] - cost[i] > 0:
        # #         tank += gas[i] - cost[i]
        # #         if tank > maxTank:
        # #             maxTank = tank
        # #             maxTankIdx = cur
        # #     else:
        # #         tank = 0
        # #         cur = i + 1
        # tank, cur = 0, 0
        # for k in range(n * 2):
        #     i = k % n
        #     if tank + gas[i] - cost[i] > 0:
        #         tank += gas[i] - cost[i]
        #         if tank > maxTank:
        #             maxTank = tank
        #             maxTankIdx = cur
        #     else:
        #         tank = 0
        #         cur = i + 1
        #     # print(k, maxTank, maxTankIdx)
        
        # # find if can complete circuit
        # tank = 0
        # for k in range(n):
        #     i = (maxTankIdx + k) % n
        #     # print(tank)
        #     tank = tank + gas[i] - cost[i]
        #     if tank < 0:
        #         return -1
        # return maxTankIdx
        '''neet
        '''
        if sum(gas) < sum(cost):
            return -1
        
        total, res = 0, 0
        for i in range(len(gas)):
            total += (gas[i] - cost[i])
            if total < 0:
                total = 0
                res = i + 1
        return res


        
            







            