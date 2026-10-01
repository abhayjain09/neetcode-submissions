class Solution:

    def encode(self, strs: List[str]) -> str:
        final = ''
        for each in strs:
            final = final + each + "abhay"

        return final
    def decode(self, s: str) -> List[str]:
        list1 = s.split("abhay")
        
        return list1[:-1]