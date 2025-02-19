class Solution:
    def listHasDuplicatesUsingSort(self, nums: list[int]) -> bool:
        nums.sort()
        for i in range(len(nums)):
            if nums[i] == nums[i - 1]:
                return True
        return False
    
    def listHasDuplicatesUsingSet(self, nums: list[int]) -> bool:
        # seen = set()
        # for num in nums:
        #     if num in seen:
        #         return True
        #     seen.add(num)
        # return False
        return len(set(nums)) < len(nums)
    
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        # return sorted(s) == sorted(t)
        
        count = [0] * 26 
        for char in s:
            count[ord(char) - ord('a')] += 1
        for char in t:
            count[ord(char) - ord('a')] -= 1

        for c in count:
            if c != 0:
                return False

    def twoSum(self, nums: list[int], target: int) -> list[int]:
        if len(nums) == 0:
            return None
        
        for i in range(len(nums)):
            diff = target - nums[i]

            if diff in nums[i+1:]:
                return [i, nums.index(diff, i+1)]
    


s = Solution()
print(s.listHasDuplicatesUsingSort([1,2,3,4]))
print(s.listHasDuplicatesUsingSort([1,2,3,3]))
print(s.listHasDuplicatesUsingSet([1,2,3,4]))
print(s.listHasDuplicatesUsingSet([1,2,3,3]))
print(s.isAnagram("vijay", "ijavy"))
print(s.isAnagram("vijay", "ijava"))
print(s.twoSum([3,4,5,6],7))
print(s.twoSum([4,5,6],10))

print(set([1,2,3,3]))

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x ]
print("List Comprehension - if: {}".format(newlist))
newlist = [x if "a" in x else "v" for x in fruits]
print("List Comprehension - if else: {}".format(newlist))
      
def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print("sort with custom function: {}".format(thislist))

thislist = ["apple", "banana", "cherry"]
mylist = thislist[:]
print( "copy: {}".format(mylist))

print( "Index of element: {}".format([4, 55, 64, 32, 16, 32].index(32)))
print( "Index of element: {}".format([4, 55, 64, 32, 16, 32].index(32,4)))

mytuple = ("apple", "banana", "cherry")
print(type(mytuple))

print(type([1,2,3,4]))


set1 = {"apple", 1,  "banana", 0, "cherry"}
set2 = {False, "google", 1, "apple", 2, True}

set3 = set1.intersection(set2)

print(set3)

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.symmetric_difference(set2)

print(set3)

# print final dest location
route = [(1,2), (2,3), (3,4)]
source, dest = zip(*route)
print(set(dest) - set(source))

str1 = "vijay"
str2 = "kumar"
name = [(a,b) for a, b in zip(str1, str2)]
print(name)
name = [a + b for a, b in zip(str1, str2)]
print(name)

# find out given 2 strings are anagram or not - approach 1
str1 = "vijay"
str2 = "yjiav"

if (len(str1) != len(str2)):
    print("not a anagram")

for s1 in str1:    
    str2 = str2.replace(s1,"",1)

if(len(str2) == 0):
    print("anagram")

# find out given 2 strings are anagram or not - approach 2
str2 = "yjiav"

for i, s1 in enumerate(str1): str2 = str2.replace(s1,str(i),1) 
try:
    str2 = int(str2)
    print("anagram")
except ValueError:
    print("Not a anagram")
# for i, s1 in range(len(str1)), str1:
    # print("i: {}, char: {}".format(i, s1))

print("print count of list numbers < current list number - approach1")
nlist = [8,2,4,5,1,8]
print(nlist)
nlistcount = [0] * len(nlist)
for i in range(len(nlist)):
    for j in range(len(nlist)):
        if(nlist[i] > nlist[j]):
            nlistcount[i] += 1
print(nlistcount)

print("print count of list numbers < current list number - approach2")
nlist = sorted(nlist, reverse="true") 
print(nlist)
list_count = [0] * len(nlist)
listlen = len(nlist)
for i in range(len(nlist)):
    list_count[i] = listlen - nlist.index(nlist[i]) - 1
    if nlist.count(nlist[i]) > 1 :
        list_count[i] -= nlist.count(nlist[i]) - 1

print(list_count)

nlist = [8,2,4,5,1,9]

print("bst - approach1")
nnlist = sorted(nlist)
print(nnlist)

def bst(num:list, target:int) -> bool:
    numlen = len(num)
    if numlen==1 and num[0] == target:
        return True

    mid = numlen//2
    if mid == 0: return False

    if num[mid] > target:
        return bst(num[:mid], target)
    elif num[mid] <= target:
        return bst(num[mid:], target)
    

print(bst(nnlist, 10))

print("bst1 - approach2")
def bst1(num:list, target:int) -> int:
    start = 0
    end = len(num)

    while(start <= end) :
        mid = (start + end) // 2
        # print("start: {}, end: {}, mid: {}".format(start, end, mid))
        if num[mid] == target:
            return mid
        elif num[mid] > target:
            end = mid - 1
        elif num[mid] < target:
            start = mid + 1
        # print("start: {}, end: {}, mid: {}".format(start, end, mid))
    return -1

print(bst1(nnlist, 4))