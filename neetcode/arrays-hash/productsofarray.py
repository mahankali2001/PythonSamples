
class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        result = []
        for i in range(len(nums)):
            val = 1
            val = [val := val * jval for j, jval in enumerate(nums) if j != i][-1]
            result.append(val)
        return result


if __name__ == "__main__":
    s = Solution()
    print(s.productExceptSelf([2,4,3,1]))
    # print(s.productExceptSelf([0,0]))