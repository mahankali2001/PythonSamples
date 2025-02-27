class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        dic,count, result = {}, 0, []
        for n in nums:
            dic[n] = dic.get(n,0) + 1
        
        dic = dict(sorted(dic.items(), key=lambda item: item[1], reverse=True))

        for num, freq in dic.items():
                count += 1
                result.append(num)
                if count == k:
                    break
        return result

if __name__ == '__main__':
    sol = Solution()
        
    print(sol.topKFrequent([1,1,1,2,2,3], 2))
    print(sol.topKFrequent([1], 1))
    print(sol.topKFrequent([1,2,3,4,5,6,7,8,9,10], 3))
    print(sol.topKFrequent([4,4,4,4,4,4,4,4,4,4], 1))
    print(sol.topKFrequent([1,2,3,4,5,6,7,8,9,10,1,2,3,4,5,6,7,8,9,10], 5))