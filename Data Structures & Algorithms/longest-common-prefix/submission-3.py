class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        output = ""
        i = 0
        for each in strs[0]:
            
            for k in strs:
             try:
                if k == "":
                    j = ""
                    return j
                elif each == k[i]:
                    pass
                else:
                    return output
             except: 
                return output
            output = output + each
            i += 1
        return output  

        