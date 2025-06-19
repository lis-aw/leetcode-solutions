class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complement = target
        complementMap = {}
        result=[]
        for idx, num in enumerate(nums):
            complement = target-num #9-2=7
            if complement in complementMap.keys():#if 7 is already a key in complementMap
                idxnumber1 = idx #first number is the number at index 0 in nums array
                idxnumber2 = complementMap[complement] #this returns the index of the complement
                result = [idxnumber1,idxnumber2]
                return result    
            else:
                complementMap[num] = idx #complementMap{2:0} store number and index of number inside nums array in this dict
        