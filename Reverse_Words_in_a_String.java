public class Solution {
    /**
     * @param s : A string
     * @return : A string
     */
    public String reverseWords(String s) {
        // write your code
        if (s == null || s.length() == 0) return "";
        StringBuilder sb = new StringBuilder();
        int ix = s.length() - 1;
        while  (ix >= 0){
            StringBuilder temp = new StringBuilder();
            while(s.charAt(ix) != ' '){
                temp.append(s.charAt(ix));
                ix--;
                if (ix < 0) break;
            }
            if (temp.length() > 0){
                temp.reverse();
                sb.append(temp);
                sb.append(" ");
            }
            ix--;
        }
        if (sb.length() > 0)
        sb.deleteCharAt(sb.length()-1);
        return sb.toString();
    }
}
