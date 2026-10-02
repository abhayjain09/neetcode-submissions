class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        k = len(nums)
        result = k * [1]
        prefix = k * [1]
        suffix = k * [1]
        prefix[0] = suffix[len(nums)-1] = 1
        for i in range(1, k):
            prefix[i] = prefix[i - 1] * nums[i - 1]
        for i in range(k - 2, -1, -1):
            suffix[i] = suffix[i + 1] * nums[i + 1]    
        for i in range(k):
            result[i] = prefix[i] *  suffix [i]
        return result