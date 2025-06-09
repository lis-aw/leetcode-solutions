class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        myDict={}
        idx=0
        for x in nums:
            if (target-x) in myDict:
                return [myDict[target-x],idx]
            myDict[x]=idx
            idx+=1




        