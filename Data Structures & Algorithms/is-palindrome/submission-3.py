class Solution:
    def isPalindrome(self, s: str) -> bool:

        text = ("".join(filter(str.isalnum, s))).lower()
        l, r = 0, len(text) -1

        while l < r:
            if text[l] == text[r]:
                l += 1
                r -= 1
            else:
                return False
            
        return True