public class Solution {
    public int maxProfit(int[] prices) {
        int n=prices.length;
        if (n<2) return 0;
        int front=1;
        int back=0;
        int res=0;
        while(front<n){
            if(prices[front]>prices[back]){
                res+=prices[front]-prices[back];
                front++;
                back++;
            }
            else{
                back=front;
                front++;
            }
        }
        return res;
    }
}