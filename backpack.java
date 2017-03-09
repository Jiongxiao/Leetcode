public class Solution {
    /**
     * @param m: An integer m denotes the size of a backpack
     * @param A: Given n items with size A[i]
     * @return: The maximum size
     */
    public int backPack(int m, int[] A) {
        // write your code here
        if (A == null || A.length == 0) return 0;
        int n = A.length;
        int [][] dp = new int [n+1][m+1];
        for (int i = 0; i<n; i++){
            for (int j = 0; j <=  m; j++){
                if (A[i] > j){
                    dp[i+1][j] = dp[i][j];
                }
                else{
                    dp[i+1][j] = Math.max(dp[i][j],dp[i][j-A[i]]+A[i]);
                }
            }
        }
        return dp[n][m];
        
        
    }
}