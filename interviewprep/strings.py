class solution:
    def findnonrepeatsubstr(self, str):
        dic, p1, p2, strlen, str_chars = {}, 0, 0, len(str), list(str)

        while p2 < strlen:
            p2 += 1
            if p2 == strlen: break
            subchar = str_chars[p1:p2]
            if str_chars[p2] in subchar:
                dic.update({"".join(subchar):len(subchar)})
                p1, p2 = p1+1, p1
                print(dic)
            
            if p2 == strlen-1:
                dic.update({"".join(str_chars[p1:p2+1]):len(str_chars[p1:p2+1])})
                print(dic)

        longstrlen, longstr = 0, ""
        for key, val in dic.items():
            if longstrlen < val:
                longstrlen = val
                longstr = key
        
        return longstr

if __name__ == "__main__":
    s = solution()
    test_str = "abcabcbb"
    result = s.findnonrepeatsubstr(test_str)
    print(f"The longest non-repeating substring in '{test_str}' is '{result}'")

    test_str = "abbcacbb"
    result = s.findnonrepeatsubstr(test_str)
    print(f"The longest non-repeating substring in '{test_str}' is '{result}'")

    test_str = "abbabcbb"
    result = s.findnonrepeatsubstr(test_str)
    print(f"The longest non-repeating substring in '{test_str}' is '{result}'")

    test_str = "abbabcbd"
    result = s.findnonrepeatsubstr(test_str)
    print(f"The longest non-repeating substring in '{test_str}' is '{result}'")


# abcabcbb
# abc, bca, cab, abc, bc, cb,b

# abbcacbb
# ab, bca, ca, acb, cb, b 

# abbabcbb
# ab, ba, abc, bc, cb, b

# abcabcbb
#     p1 = 0, P2 = 0 => P1 Vs P2+1 => a Vs b => P2 = 1
#     P1 = 0, P2 = 1 => a vs c => p2 = 2
#     p1 = 0, p2 = 2 => a vs a => p1 = p2
#     p1 = 2, p2 = 2 => a vs b => P2 = 3
#     p1 = 2, p2 = 3 => a vs c => p2 = 4
#     p1 = 2, p2 = 4 => a vs b => 