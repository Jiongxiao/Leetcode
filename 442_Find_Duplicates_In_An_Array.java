public class Solution {
    public List<Integer> findDuplicates(int[] nums) {
        int n=nums.length;
        for (int i=0; i<n; i++){
            nums[nums[i]%(n+1)-1]+=n+1;
        }
        List <Integer> res= new ArrayList<>();
        for(int i=0;i<n;i++){
            if (nums[i]>2*(n+1)) res.add(i+1);
        }
        return res;
    }
}