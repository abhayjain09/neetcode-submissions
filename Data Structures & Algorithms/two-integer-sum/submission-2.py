class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #dic solution o(n)
        dic = {}
        for i, j in enumerate(nums):
            diff = j - target
            if diff in dic:
                return [dic[diff], i]

            dic[diff] = i
            
        ##my solution 0(n^2)
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]
        