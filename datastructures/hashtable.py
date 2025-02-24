list1 = [1,3,5]
list2 = [2,4,5]

def item_in_common(l1, l2):
    for l1item in l1:
        if l1item in l2:
            return True
    return False

print("item_in_common:")
print(item_in_common(list1, list2))


def find_duplicates(l1):
    dups = {}
    for l1item in l1:
        dups[l1item] = dups.get(l1item, 0) + 1
    
    return [key for key, val in dups.items() if val > 1 ]

print("find_duplicates:")
print ( find_duplicates([1, 2, 3, 4, 5]) )
print ( find_duplicates([1, 1, 2, 2, 3]) )
print ( find_duplicates([1, 1, 1, 1, 1]) )
print ( find_duplicates([1, 2, 3, 3, 3, 4, 4, 5]) )
print ( find_duplicates([1, 1, 2, 2, 2, 3, 3, 3, 3]) )
print ( find_duplicates([1, 1, 1, 2, 2, 2, 3, 3, 3, 3]) )
print ( find_duplicates([]) )


def first_non_repeating_char(str):
    for char in str:
        index = str.index(char)
        try:
            if str.index(char, index+1) > 0:
                continue
        except ValueError:
            return char
        # if str.count(char) == 1:
        #     return char
    return None

print("first_non_repeating_char:")
print( first_non_repeating_char('leetcode') )
print( first_non_repeating_char('hello') )
print( first_non_repeating_char('aabbcc') )

# Group Anagrams

# Tow Sum

# Subarray Sum
def subarray_sum(nums, target):
    sum, start, end = 0, 0, 0
    if len(nums) == 0: return []
    while True:
        if end < len(nums):
            sum += nums[end]
            if sum == target:    
                return [start, end]
            end += 1
        else:
            start += 1
            if start == len(nums): break
            sum = 0
            end = start

    return []


print("subarray_sum:")
nums = [1, 2, 3, 4, 5]
target = 9
print ( subarray_sum(nums, target) )

nums = [-1, 2, 3, -4, 5]
target = 0
print ( subarray_sum(nums, target) )

nums = [2, 3, 4, 5, 6]
target = 3
print ( subarray_sum(nums, target) )

nums = []
target = 0
print ( subarray_sum(nums, target) )


# Using sets
def has_unique_chars(string):
    char_set = set()
    for char in string:
        if char in char_set:
            return False
        char_set.add(char)
    return True

# def has_unique_chars(str):
#     for char in str:
#         if str.count(char) > 1:
#             return False
#     return True
    # print(list(str))
    # print("".join(set(str)))
    # return len(set(str)) == len(str)

print("has_unique_chars:")
print(has_unique_chars('abcdefg')) # should return True
print(has_unique_chars('hello')) # should return False
print(has_unique_chars('')) # should return True
print(has_unique_chars('0123456789')) # should return True
print(has_unique_chars('abacadaeaf')) # should return False

# Using sets
def find_pairs(arr1, arr2, target):
    pairlist = []
    for i, ival in enumerate(arr1):
        for j, jval in enumerate(arr2):
            if ival + jval == target:
                pairlist.append((ival,jval))

    return pairlist

    # return [(i, j)
    #         for i in range(len(arr1)) 
    #             for j in range(len(arr2)) 
    #                 if arr1[i] + arr2[j] == target]


arr1 = [1, 2, 3, 4, 5]
arr2 = [2, 4, 6, 8, 10]
target = 7

pairs = find_pairs(arr1, arr2, target)
print (pairs)

# Using sets
def longest_consecutive_sequence(mylist):
    slist = sorted(mylist)
    # print(slist)
    maxconseq, seqset = 0, set()
    for i in range(len(slist)):
        if len(seqset) == 0:
            seqset.add(slist[i])
        if slist[i]+1 in slist:
            seqset.add(slist[i+1])
        else:
            if maxconseq < len(seqset):
                maxconseq = len(seqset)
            seqset.clear()
    return maxconseq

print("longest_consecutive_sequence:")
print( longest_consecutive_sequence([100, 4, 200, 1, 3, 2]) )
print( longest_consecutive_sequence([100, 4, 200, 6, 8, 10]) )
print( longest_consecutive_sequence([100]) )