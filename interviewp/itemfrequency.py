from itertools import combinations

class solution:
    def calItemFrequency(self, items:list):
        dic = {}
        for i in items:
            # print (tuple(i))
            if tuple(i) in dic:
                dic[tuple(i)] += 1
            else:
                dic[tuple(i)] = 1
            
            # print(len(i)-1)
            for k in range(1, len(i)-1):
                for j in combinations(i, k+1):
                    # print(j)
                    if j in dic:
                        dic[j] += 1 
                    else:
                        dic[j] = 1 
        
        return dic
        # for key, value in dic.items():
        #     print(", ".join(key), "-", value)

if __name__ == "__main__":
    # input
    trans = [["apple", "banana", "lemon"], ["banana", "berry", "lemon", "orange"], ["banana", "berry", "lemon"]]
    s = solution()
    result = s.calItemFrequency(trans)
    for key, value in result.items():
        print("{} - {}".format(key,value))


# output
# apple, banana, lemon - 1
# apple, banana - 1
# apple, lemon - 1
# banana, lemon - 3

# banana, berry, lemon, orange - 1
# banana, berry - 2
# banana, orange - 1
# berry, lemon - 2
# berry, orange - 1
# lemon, orange - 1

# banana, berry, lemon - 2
# banana, berry, orange - 1
# banana, lemon, orange - 1
# berry, lemon, orange - 1