public class Solution {
    public String decodeString(String s) {
        Stack<Integer> num= new Stack<>();
        Stack<String> string= new Stack<>();
        int count=0;
        StringBuilder res=new StringBuilder();
        for (int i=0; i<s.length();i++){
            char ch=s.charAt(i);
            if (Character.isDigit(ch)){
                count=count*10+Character.getNumericValue(ch);
            }
            else if (ch=='['){
                string.push(res.toString());
                num.push(count);
                res.setLength(0);
                count=0;

            }
            else if (ch==']'){
                StringBuilder temp=new StringBuilder(string.pop());
                int repeat= num.pop();
                for (int j=0; j<repeat;j++){
                    temp.append(res);
                }
                res=temp;
            }
            else{
                res.append(ch);
            }
        }
        return res.toString();
    }
}