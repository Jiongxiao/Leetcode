public class Solution {
    public int arrangeCoins(int n) {
        int result=0;
        int root=(int) (Math.sqrt(n)*Math.sqrt(2)+1); // 32-digit
        System.out.println(root);
        for(int i=root; i>=0; i--){
            if (i*(i+1)<=2*n){
                return i;
            }
        }
        return result;
    }
}