class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
          dic = {}
          for each in strs:
            string_sort = tuple(sorted(each))
            if string_sort not in dic:
                dic[string_sort] = []
            dic[string_sort].append(each)
          return list(dic.values())
