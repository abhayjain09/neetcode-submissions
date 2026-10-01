class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}
        final_list = []
        for i in nums:
            dic[i] = 1 + dic.get(i, 0)
        sorted_data = list((dict(sorted(dic.items(), key = lambda item: item[1], reverse=True ))).keys())

        return sorted_data[:k]