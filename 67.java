public class Solution {
    public String addBinary(String a, String b) {
        int l=a.length();
        int r=b.length();
        int i=0, carry=0;
        StringBuilder res=new StringBuilder();
        while(i<l || i<r || carry!=0){
            int x= (i<l) ? Character.getNumericValue(a.charAt(l-i-1)):0;
            int y= (i<r) ? Character.getNumericValue(b.charAt(r-i-1)):0;
            res.append((x+y+carry)%2);
            carry=(x+y+carry)/2;
            i++;
        }
        return res.reverse().toString();
    }
}