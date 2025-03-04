import re

class Solution:
    # case-insensitive and ignores all non-alphanumeric characters
    def isPalindrome(self, s: str) -> bool:
        # word_specialCharsToStripRegex = r'[.,!?;()[]]' 
        # s = s.strip(word_specialCharsToStripRegex).lower().replace(" ", "") # this does not fix ` and , characters
        
        word_specialCharsToStripRegex = r'[^a-zA-Z0-9]'
        s = re.sub(word_specialCharsToStripRegex, '', s).lower()

        l = len(s)
        print(s, l)
        for i in range(len(s)):
            if s[i] != s[l-1] and i < l-1:
                return False
            l -= 1

        return True
    
        
if __name__ == "__main__":
    s = Solution()
    print(s.isPalindrome("Was it a car or a cat I saw?"))
    print(s.isPalindrome("vijayyajiv"))
    print(s.isPalindrome("Madam, in Eden, I'm Adam"))