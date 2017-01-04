public class Solution {
    public int findMaximumXOR(int[] nums) {
        int res=0;
        for (int i=31;i>=0;i--){
            res=res<<1;
            Set<Integer> set=new HashSet<>();
            for (int num : nums){
                set.add(num>>i);
            }
            int temp=res+1;
            for(int x: set){
                if (set.contains(temp^x)){
                    res=temp;
                    break;
                }
            }
            
        }
        return res;
    }
}