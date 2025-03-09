class Solution(object):    
    def trapwater(self, height: list[int]) -> int:
        '''Two pointer approach'''
        if not height:
            return 0
        n = len(height)
        res = 0

        for i in range(n):
            leftMax = rightMax = height[i]

            for j in range(i):
                leftMax = max(leftMax, height[j])
            for j in range(i + 1, n):
                rightMax = max(rightMax, height[j])
                
            res += min(leftMax, rightMax) - height[i]
        return res
        
        # i, l, ndic = 0, len(height), {}
        # for i, val in enumerate(height):
        #     if i != 0 and i != l-1:
        #         minval = min(max(height[:i]), max(height[i:])) 
        #         ndic[i] = (lambda minval, val: 0 if minval-val < 0 else minval-val)(minval, val)

        # print(ndic)
        # return sum(map(lambda item: item[1], ndic.items()))

if __name__ == "__main__":
    s = Solution()
    print(s.trapwater([1,7,2,5,4,7,3,6]))
    print(s.trapwater([0,2,0,3,1,0,1,3,2,1]))