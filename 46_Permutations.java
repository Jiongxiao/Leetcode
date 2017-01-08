public class Solution {
    public List<List<Integer>> permute(int[] nums) {
        List<List<Integer>> ans=new ArrayList<List<Integer>>();
        if(nums.length==0) return ans;
        List<Integer> l0= new ArrayList<>();
        l0.add(nums[0]);
        ans.add(l0);
        for (int i=1; i< nums.length; i++){
            List<List<Integer>> new_ans=new ArrayList<List<Integer>>();
            for (int j=0; j<=i;j++){
                for (List<Integer> l : ans){
                    List<Integer> new_l=new ArrayList<>(l);
                    new_l.add(j,nums[i]);
                    new_ans.add(new_l);
                }
            }
            ans=new_ans;
        }
        return ans;
    }
}

public List<List<Integer>> permute(int[] num) {
    LinkedList<List<Integer>> res = new LinkedList<List<Integer>>();
    res.add(new ArrayList<Integer>());
    for (int n : num) {
        int size = res.size();
        for (; size > 0; size--) {
            List<Integer> r = res.pollFirst();
            for (int i = 0; i <= r.size(); i++) {
                List<Integer> t = new ArrayList<Integer>(r);
                t.add(i, n);
                res.add(t);
            }
        }
    }
    return res;
}