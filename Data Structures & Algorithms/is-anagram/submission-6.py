class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ### solution 1
        return Counter(s) == Counter(t)

        if len(s) != len(t):
            return False
        dic  = {}
        dic1 = {}
        for i in range(len(s)):
            if s[i] in dic:
                dic[s[i]] = dic[s[i]] + 1
            else:
                dic[s[i]] = 1
            if t[i] in dic1:
                dic1[t[i]] = dic1[t[i]] + 1
            else:
                dic1[t[i]] = 1  

        
        return dic1 == dic
        