from collections import defaultdict
from collections import Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        collectAnagrams=defaultdict(list)
        for val in strs:
            y=frozenset(Counter(val).items())
            collectAnagrams[y].append(val)

        return(list(collectAnagrams.values()))


