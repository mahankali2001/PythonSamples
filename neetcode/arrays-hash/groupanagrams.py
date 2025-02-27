class solution:
    def groupAnagrams(self,strs):
        anagrams = []
        covered_strings = []
        
        for s1 in strs:
            alist = []
            for s2 in strs:
                if s1 == s2 or s2 in covered_strings: continue
                # if isAnagram(s1,s2):
                if sorted(s1) == sorted(s2):
                    if len(alist) == 0:
                        alist.append(s1)
                    alist.append(s2)
                    covered_strings.extend(alist)
            if len(alist) > 0:
                anagrams.append(alist)
            elif s1 not in covered_strings:
                anagrams.append([s1])

        return anagrams

    def groupAnagramsHM(self,strs):
        covered_strings = {}
        
        for s1 in strs:
            key = ''.join(sorted(s1))
            if key in covered_strings:
                covered_strings[key].append(s1)
            else:
                covered_strings[key] = [s1]
            
            # key = tuple(sorted(s1))
            # if key in covered_strings:
            #     covered_strings[key].append(s1)
            # else:
            #     covered_strings[key] = [s1]

        return list(covered_strings.values())

    # def isAnagram(self, str1, str2):
    #     return sorted(str1) == sorted(str2)
    #     # for c in str1:
    #     #     if c in str2:
    #     #         str2 = str2.replace(c, '', 1)
    #     #     else:
    #     #         return False
    #     # return str2 == ''



s = solution()
strs = ["act","pots","tops","cat","stop","hat"]
print(s.groupAnagrams(strs))
print(s.groupAnagramsHM(strs))