class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        list_nums = sorted(nums)
        list_nums = list(dict.fromkeys(list_nums))  # Remove duplicates while preserving order
        if len(list_nums) == 1:
            return 1
        final_result = 1
        k = 0
        result = 1
        print(list_nums)
        while k < len(list_nums) - 1:
            if list_nums[k+1] == (list_nums[k] + 1):
                result += 1
            else:                
                final_result = max(final_result, result)
                result = 1  
            k += 1
        return max(final_result, result)
        