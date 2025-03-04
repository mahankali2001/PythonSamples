class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        slist, max, count, prev = sorted(nums), 0, 0, -99
        # print(slist)
        for val in slist:
            # print(prev, val)
            if prev == -99:
                prev = val
                count += 1
                continue
            if prev == val:
                continue
            elif prev + 1 == val:
                count += 1
                prev = val
            else:
                if max < count:
                    max = count
                prev = val
                count = 1
        if max < count:
            max = count
        return max


if __name__ == "__main__":
    s = Solution()
    print(s.longestConsecutive([2,20,4,10,3,4,5]))
    print(s.longestConsecutive([0,3,2,5,4,6,1,1]))