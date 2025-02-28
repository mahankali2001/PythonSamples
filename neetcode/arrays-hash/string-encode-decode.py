import base64

class Solution:

    def encode(self, strs: list[str]) -> str:
        if len(strs) == 0:
            return None
        if strs[0] == "":
            return ""

        # str = ','.join(strs)
        # return str
        
        str = ','.join(strs)
        encoded_bytes = base64.b64encode(str.encode('utf-8'))
        return encoded_bytes

        # if not strs:
        #     return ""
        # sizes, res = [], ""
        # for s in strs:
        #     sizes.append(len(s))
        # for sz in sizes:
        #     res += str(sz)
        #     res += ','
        # res += '#'
        # for s in strs:
        #     res += s
        # return res


    def decode(self, s: str) -> list[str]:
        if s == None:
            return []
        if s == "":
            return [""]
        
        # return s.split(",")
        
        decoded_str = base64.b64decode(s)
        decoded_str = decoded_str.decode('utf-8')
        return decoded_str.split(",")
    
        # if not s:
        #     return []
        # sizes, res, i = [], [], 0
        # while s[i] != '#':
        #     cur = ""
        #     while s[i] != ',':
        #         cur += s[i]
        #         i += 1
        #     sizes.append(int(cur))
        #     i += 1
        # i += 1
        # for sz in sizes:
        #     res.append(s[i:i + sz])
        #     i += sz
        # return res

if __name__ == "__main__":
    s = Solution()
    str = s.encode(["neet","code","love","you"])
    # str = s.encode([])
    # str = s.encode([""])
    print(str)
    print(s.decode(str))