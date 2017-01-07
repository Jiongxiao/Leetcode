public class Solution {
    public int combinationSum4(int[] nums, int target) {
        if (target==0) return 1;
        int res=0;
        for (int i=0; i<nums.length;i++){
            if (target>=nums[i]){
                res+=combinationSum4(nums,target-nums[i]);
            }
        }
        return res;
    }
}  // timelimit exceed

public class Solution {
    public int combinationSum4(int[] nums, int target) {
        int [] im= new int [target+1];
        im[0]=1;
        for (int i=1; i<im.length; i++){
            for (int j=0; j<nums.length;j++){
                if (nums[j]<=i){
                    im[i]+=im[i-nums[j]];
                }
            }
        }
        return im[target];
    }
}