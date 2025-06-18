from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countedNums = Counter(nums)
        x = sorted(countedNums.items(), key=lambda x: -x[1])
        result=[]
        for i in range(k):
            result.append(x[i][0])
        return result
        
        