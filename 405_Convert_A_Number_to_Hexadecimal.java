public class Solution {
    public String toHex(int num) {
        if (num==0) return "0";
        StringBuilder sb=new StringBuilder();
        while(num!=0){
            int temp=num&15;
            sb.append(temp<10? String.valueOf(temp) : (char) (temp-10+'a'));
            num>>>=4;
        }
        return sb.reverse().toString();
    }
}