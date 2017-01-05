public class Solution {
    public int fourSumCount(int[] A, int[] B, int[] C, int[] D) {
        int n=A.length;
        if (n==0) return 0;
        int [] l1=new int[n*n];
        int [] l2=new int[n*n];
        HashMap<Integer,Integer> map= new HashMap<>();
        for (int i=0; i<n; i++){
            for (int j=0; j<n; j++){
                int sum=A[i]+B[j];
                map.put(sum,map.getOrDefault(sum,0)+1);
            }
        }
        int res=0;
        for (int i=0; i<n;i++){
            for (int j=0; j<n; j++){
                res+=map.getOrDefault(-(C[i]+D[j]),0);
            }
        }
        return res;
    }
}