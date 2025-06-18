class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        output = [1] * length #the first entry is always 1. Also needed for *= operation
        prefix=nums[0] #first prefix is first number in nums
        postfix=nums[-1] #first postfix is last number in nums

        i=1#starting at the second entry
        while i < length:
            output[i]*=prefix
            prefix*=nums[i]
            i+=1
        #print(f"Prefix-Output: {output}")

        i=2#starting at the second to last entry
        while i <= length:
          output[-i]*=postfix
          postfix*=nums[-i]  
          i+=1
        #print(f"Postfix-Output: {output}")
        return output
        
        