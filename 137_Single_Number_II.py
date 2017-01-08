public class Solution {
    public int singleNumber(int[] nums) {
        int x1=0;
        int x2=0;
        int mask=0;
        for (int i: nums){
            x2^=x1 & i;
            x1^=i;
            mask=~(x1&x2);
            x1 &= mask;
            x2 &= mask;
        }
        return x1;
    }
}