class solution:
    def mergeSortedArrays(self, a1, a2):
        a3 = []
        a1c = 0
        a2c = 0

        while a1c < len(a1):
            if a2c == 4:
                a3.append(a1[a1c])
                a1c += 1
            else:
                while a2c < len(a2):
                    # print("IW a1c: {}, a2c: {} ".format(a1c, a2c))
                    if a1[a1c] < a2[a2c]:
                        a3.append(a1[a1c])
                        a1c += 1
                        break;
                    else:
                        a3.append(a2[a2c])
                        a2c += 1
            # print("OW a1c: {}, a2c: {} ".format(a1c, a2c))
        if a2c == 3:
            a3.append(a2[a2c])
            a2c += 1
        # print("O a1c: {}, a2c: {} ".format(a1c, a2c))
        return a3

        # a1.extend(a2)
        # return (sorted(a1))
                
if __name__ == "__main__":
    s = solution()
    a1 = [1,4,8,9]
    a2 = [2,3,6,10]
    print(s.mergeSortedArrays(a1, a2))

    a1 = [1,4,7,9]
    a2 = [2,3,6,8]
    print(s.mergeSortedArrays(a1, a2))