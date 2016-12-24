public class Solution {
    public int totalHammingDistance(int[] nums) {
       int n=nums.length;
       int [] bit=new int[32];
       for (int num: nums){
           int i=0;
           while(num>0){
               if ((num&1)==1){
                   bit[i]+=1;
               }
               i++;
               num=num>>1;
           }
       }
       int result=0;
       for (int i=0;i<32;i++){
           result+=bit[i]*(n-bit[i]);
       }
       return result;
    }
}