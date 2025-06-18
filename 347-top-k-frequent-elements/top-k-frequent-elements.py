from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countedNums = Counter(nums)
        mostCommon = countedNums.most_common(k)
        result = [num for num,count in mostCommon]
        return result
        
        