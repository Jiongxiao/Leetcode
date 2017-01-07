public class Solution {
    public String addStrings(String num1, String num2) {
        int n1=num1.length()-1;
        int n2=num2.length()-1;
        StringBuilder res= new StringBuilder();
        int sum=0;
        while(n1>=0 || n2>=0){
            if(n1>=0) sum+=Integer.parseInt(num1.substring(n1,n1+1));
            if(n2>=0) sum+=Integer.parseInt(num2.substring(n2,n2+1));
            res.append(sum%10);
            sum=sum/10;
            n1--;
            n2--;
        }
        if(sum>0) res.append(sum);
        return res.reverse().toString();
    }
}