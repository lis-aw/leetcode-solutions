class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapNumsIndex={}
        currentIndex=0
        for currentValue in nums:
            complement = target-currentValue
            if (complement) in mapNumsIndex:
                complementIndex = mapNumsIndex[complement]
                return [complementIndex,currentIndex] #returns two indices, the one of the complement, and the current one 
            mapNumsIndex[currentValue]=currentIndex #dict that saves an item of nums (key) with its index(value)
            currentIndex+=1 #increment the index




        