class Solution:
    def isPalindrome(self, s: str) -> bool:
        text = ("".join(filter(str.isalnum, s))).lower()
        return text == text[::-1]