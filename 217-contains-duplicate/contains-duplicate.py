class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        x=len(nums)
        y=len(set(nums))
        return False if x == y else True
        
        