public class Solution {
    public int minMoves2(int[] nums) {
        int n=nums.length;
        if (n==0) return 0;
        int res=0;
        Arrays.sort(nums);
        int j=n-1;
        for (int i=0;i<n/2;i++){
            res+=nums[j]-nums[i];
            j--;
        }
        return res;
    }
}