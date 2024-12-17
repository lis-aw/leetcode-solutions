import java.util.HashSet; // Import the HashSet class

class Solution {
    public int lengthOfLongestSubstring(String string) {
        HashSet<Character> duplicates = new HashSet<>();
        int l = 0;
        int result = 0;

        for (int r = 0; r < string.length(); r++) {
            while (duplicates.contains(string.charAt(r))){
                duplicates.remove(string.charAt(l));
                l++;
            }
            duplicates.add(string.charAt(r));
            result = Math.max(result, r-l + 1);
        }
        return result;
    }
}