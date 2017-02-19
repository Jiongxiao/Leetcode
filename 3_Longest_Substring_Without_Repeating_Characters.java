public class Solution {
    public int lengthOfLongestSubstring(String s) {
        int res=0;
        int i=0,j=0;
        Set<Integer> set=new HashSet<>();
        while(j<s.length()){
            if (!set.contains(s.charAt(j))){
                set.add(s.charAt(j++));
                res=Math.max(set.size(),res);
            }
            else{
                set.remove(s.charAt(i++));
            }
        }
        return res;
    }
}