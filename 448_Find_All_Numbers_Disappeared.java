public class Solution {
    public List<Integer> findDisappearedNumbers(int[] nums) {
        for (int i=0;i<nums.length;i++){
            if ((nums[Math.abs(nums[i])-1])>0)
            nums[Math.abs(nums[i])-1]=-nums[Math.abs(nums[i])-1];
        }
        ArrayList<Integer> result = new ArrayList<Integer>();
        for (int j=0;j<nums.length;j++){
            if (nums[j]>0)
            result.add(j+1);
        }
        return result;
    }
}