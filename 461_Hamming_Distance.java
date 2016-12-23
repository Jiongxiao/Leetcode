public class Solution {
    public int hammingDistance(int x, int y) {
        int z=x^y;
        return Integer.bitCount(z);
    }
}


public class Solution {
    public int hammingDistance(int x, int y) {
        int z=x^y;
        int count=0;
        while(z!=0){
            if((z>>1)<<1!=z) count++;
            z=z>>1;
        }
        return count;
    }
}