class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        k = set(nums)
        return len(k) != len(nums)
        