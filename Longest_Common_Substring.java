public class Solution {
    /**
     * @param A, B: Two string.
     * @return: the length of the longest common substring.
     */
    public int longestCommonSubstring(String A, String B) {
        // write your code here
        if (A == null || B == null || A.isEmpty() || B.isEmpty()) return 0;
        int n = A.length(), m = B.length();
        int[][] dp = new int[n + 1][m + 1];
        for (int i = 1; i <= n; i++){
            for (int j = 1; j <= m; j++){
                if (A.charAt(i-1) == B.charAt(j-1)){
                    dp[i][j] = dp[i - 1][j - 1]+1;
                }
            }
        }
        int res = 0;
        for (int i = 1; i <= n; i++){
            for (int j = 1; j <= m; j++){
                if (dp[i][j] > res){
                    res = dp[i][j];
                }
            }
        }
        return res;
    }
}