class Solution(object):    
    def maxArea(self, heights: list[int]) -> int:
        i, j, l, max, ndic = 0, 1, len(heights), 0, {}
        # print (l, m)
        while j <  l:
            
            ndic[(i ,j)] = min(heights[i], heights[j]) * (j-i)
            if ndic[(i ,j)] < 0:
                ndic[(i ,j)] = ndic[(i ,j)] * -1
            j += 1

            if j==l:
                i += 1
                j = i+1
        
        for val in ndic.values():
            if val > max:
                max = val

        return  max

if __name__ == "__main__":
    s = Solution()
    print(s.maxArea([1,7,2,5,4,7,3,6]))
    print(s.maxArea([2,2,2]))