from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        collectAnagrams = defaultdict(list)
        for val in strs:
            count = [0] * 26
            for c in val:
                count[ord(c) - ord("a")] += 1  
            collectAnagrams[tuple(count)].append(val)
        return list(collectAnagrams.values())



