from collections import defaultdict
from collections import Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        allSets=[]
        collectAnagrams=defaultdict(list)
        idx=0
        for val in strs:
            x=Counter(val)
            y=frozenset(x.items())
            collectAnagrams[y].append(val)

        return(list(collectAnagrams.values()))


