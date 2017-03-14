public class Solution {
    /**
     * @param str: an array of char
     * @param offset: an integer
     * @return: nothing
     */
    public void rotateString(char[] str, int offset) {
        // write your code here
        for (int i = 0; i < offset; i++){
            rotate(str);
        }

    }
    public void rotate(char[] str){
        if (str.length < 2) return;
        char temp = str[str.length - 1];
        for (int i = str.length - 1; i > 0; i--){
            str[i] = str[i-1];
        }
        str[0] = temp;
    }
}//////////////////超时

public class Solution {
    /**
     * @param str: an array of char
     * @param offset: an integer
     * @return: nothing
     */
    public void rotateString(char[] str, int offset) {
        // write your code here
        int n = str.length;
        if (n < 2) return;
        offset = offset % n;
        rotate(str,0,n - offset - 1);
        rotate(str,n - offset, n-1);
        rotate(str,0,n-1);
    }
    
    public void rotate(char[] str, int start, int end){
        while(start < end){
            char temp = str[end];
            str[end] = str[start];
            str[start] = temp;
            start++;
            end--;
        }
    }
}