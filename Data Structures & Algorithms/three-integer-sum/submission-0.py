class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        length = len(nums)
        nums.sort()
        final_result = []
        for i in range(length - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            target = nums[i]
            j = i + 1
            k = length - 1
            while j < k:
                curSum = -(nums[j] + nums[k])
                if curSum > target:
                    j += 1
                elif curSum < target:
                    k -= 1
                else:
                    final_result.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1

                    while j < k and nums[j] == nums[j - 1]:
                        j += 1

                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1
        
        return final_result                    
