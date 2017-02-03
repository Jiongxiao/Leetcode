public class Solution {
    public List<String> generateParenthesis(int n) {
        List<String> res= new ArrayList<>();
        backtract(res,"",0,0,n);
        return res;

    }
    public void backtract(List<String> res, String s, int left, int right, int n){
        if (s.length()==2*n) {
            res.add(s);
            return;
        }
        if (left<n) backtract(res,s+"(",left+1,right,n);
        if (left>right) backtract(res,s+")",left,right+1,n);
    }
}