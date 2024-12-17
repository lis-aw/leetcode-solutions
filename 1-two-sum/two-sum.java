class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> twoSumMap = new HashMap<>();
        
        for (int i = 0; i < nums.length; i++) {
            
            int complement = target - nums[i];
            boolean contains = (twoSumMap.containsKey(complement));
            if (contains) {
                    return new int[]{twoSumMap.get(complement), i}; // Return indices of complement and current number
                }
                twoSumMap.put(nums[i], i);
          }

            
        return null; // Return null if no solution is found
    }
}