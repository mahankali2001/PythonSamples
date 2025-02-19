class Solution(object):    
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            val = nums[i]
            diff = target - val
            if diff > 0:                
                try:
                    j = nums.index(diff)

                    if i < j:
                        return [i,j]
                    else:
                        return [j,i]
                except ValueError:
                    continue
s = Solution()
print(s.twoSum([2,7,11,15], 9))
print(s.twoSum([2,7,11,15], 26))
print(s.twoSum([15,11,2,7], 26))