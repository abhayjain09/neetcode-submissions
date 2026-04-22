class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        length = int (len(s)/2)
        j = len(s) - 1
        for i in range(length):
            temp = s[i]
            s[i] = s[j]
            s[j] = temp
            j -= 1
        
        
