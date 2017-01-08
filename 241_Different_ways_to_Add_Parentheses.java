public class Solution {
    public List<Integer> diffWaysToCompute(String input) {
        List <Integer> res= new ArrayList<Integer>();
        for (int i=0; i<input.length();i++){
            char c= input.charAt(i);
            if (c=='+' || c=='-' || c=='*'){
                List<Integer> left= diffWaysToCompute(input.substring(0,i));
                List<Integer> right= diffWaysToCompute(input.substring(i+1));
                for (int x :left){
                    for (int y: right){
                        if (c =='+') res.add(x+y);
                        if (c=='-') res.add(x-y);
                        if (c=='*') res.add(x*y);
                    }
                }
            }
        }
        if (res.size()==0) res.add(Integer.parseInt(input));
        return res;
    }
}