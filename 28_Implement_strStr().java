public class Solution {
    public int strStr(String haystack, String needle) {
        if (haystack == null && needle == null) return 0;
        if (haystack == null) return -1;
        if (needle == null) return 0;
        
        for (int i = 0; i < (haystack.length() - needle.length() + 1); i++ ){
            
            int j = 0;
            for (; j < needle.length(); j++){
                if (haystack.charAt(i+j) != needle.charAt(j)){
                    break;
                }
            }
            if (j == needle.length()) return i;
        }
        return -1;
    }
    
}


public class Solution {
    public int strStr(String haystack, String needle) {
        if (haystack == null && needle == null) return 0;
        if (haystack == null) return -1;
        if (needle == null) return 0;
        if (needle.length()==0) return 0;
        int [] next = getNext(needle);
        int i = 0, j = 0;
        while(i < haystack.length() && j < needle.length()){
            if (j == -1 || haystack.charAt(i) == needle.charAt(j)){
                i++;
                j++;
            }
            else{
                j = next[j];
            }
        }
        if (j == needle.length()){
            return i-j;
        }
        else return -1;
        
    }

    public int[] getNext(String target){
        int[] next = new int[target.length()];
        next[0] = -1;
        int k = -1, j = 0;
        while(j < target.length() - 1){
            if (k == -1 || target.charAt(j) == target.charAt(k)){
                next[++j] = ++k;
            } else{
                k = next[k];
            }
        }
        return next;
    }
    
}