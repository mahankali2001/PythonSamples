class Solution(object):    
    def threesum(self, nums):
        i, j, k, l, nlist = 0, 1, 2, len(nums), []
        while k < l:
            if nums[i] + nums[j] + nums[k] == 0 and sorted([nums[i], nums[j], nums[k]]) not in nlist :
                nlist.append(sorted([nums[i], nums[j], nums[k]]))
            # j += 1
            k += 1 
            
            if k > l-1 and j < l-2:
                j += 1 
                k = j + 1
            elif k > l-1:
                i += 1
                j = i+1
                k = j+1
            
        return nlist

s = Solution()
print(s.threesum([-1,0,1,2,-1,-4]))
print(s.threesum([0,1,1]))
print(s.threesum([0,0,0]))
print(s.threesum([0,0,0,0]))
print(s.threesum([-2,0,1,1,2]))