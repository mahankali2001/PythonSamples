class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        '''sliding window'''
        res = 0
        for i in range(len(prices)):
            buy = prices[i]
            for j in range(i + 1, len(prices)):
                sell  = prices[j]
                res = max(res, sell - buy)
        return res
        
        '''split, lambda, map, max'''
        # ndic = {}
        # for i, val in enumerate(prices):
        #     ndic[i] = max(prices[i:]) - val
        
        # return max(map(lambda item: item[1], ndic.items()))

if __name__ == "__main__":
    s = Solution()
    print(s.maxProfit([10,1,5,6,7,1]))
    print(s.maxProfit([10,8,7,5,2]))
