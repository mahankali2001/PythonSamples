class Solution(object):    
    def twoSum(self, nums, target):
        i, j, l = 0, 1, len(nums)
        while i < l:
            if nums[i] + nums[j] == target:
                return [i, j]
            else:
                j += 1
                if j == l:
                    i += 1
                    j = i+1
        return None

if __name__ == "__main__":                
    s = Solution()
    print(s.twoSum([2,7,11,15], 9))
    print(s.twoSum([2,7,11,15], 26))
    print(s.twoSum([15,11,2,7], 26))