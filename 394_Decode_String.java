public class Solution {
    public String decodeString(String s) {
        Stack<Integer> num= new Stack<>();
        Stack<String> string= new Stack<>();
        int count=0;
        String res="";
        for (int i=0; i<s.length();i++){
            char ch=s.charAt(i);
            if (Character.isDigit(ch)){
                count=count*10+Character.getNumericValue(ch);
            }
            else if (ch=='['){
                string.push(res);
                num.push(count);
                res="";
                count=0;

            }
            else if (ch==']'){
                StringBuilder temp=new StringBuilder(string.pop());
                int repeat= num.pop();
                for (int j=0; j<repeat;j++){
                    temp.append(res);
                }
                res=temp.toString();
            }
            else{
                res+=ch;
            }
        }
        return res;
    }
}