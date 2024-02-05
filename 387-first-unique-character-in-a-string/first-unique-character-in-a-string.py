class Solution:
    def firstUniqChar(self, s: str) -> int:
        obj = {}
        for i in range(len(s)):
            ch = s[i]
            if (ch in obj.keys()):
                obj[ch]+=1
            else: obj[ch]=1
        for i in range(len(s)):
            
            if obj[s[i]] == 1:
                return i
        return -1