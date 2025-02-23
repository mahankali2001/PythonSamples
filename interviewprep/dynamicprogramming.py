class dynamicprogramming:
    def __init__(self):
        pass

    def maxrobberymoney(self, money):
        if not money:
            return 0
        
        rh = [0] * len(money)
        maxrobval = 0
        for i in range(len(money)):
            if i ==0:
                rh[i] = money[i]
            else:
                if i-2 >= 0:
                    rh[i] = max(money[i]+ rh[i-2], rh[i-1])
                else:
                    rh[i] = max(money[i], rh[i-1])
            if maxrobval < rh[i]:
                maxrobval = rh[i]
        print(maxrobval)

if __name__ == "__main__":
    dp = dynamicprogramming()
    
    money = [2, 7, 9, 3, 1]
    dp.maxrobberymoney(money)

    money = [10, 1, 9, 3, 12, 7, 4]
    dp.maxrobberymoney(money)