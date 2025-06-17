from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        collectAnagrams = defaultdict(list)
        for val in strs:
            key = ''.join(sorted(val))  # O(K log K)
            collectAnagrams[key].append(val)
        return list(collectAnagrams.values())



