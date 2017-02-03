/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
public class Solution {
    Map<Integer,Integer> count;
    int max=0;
    public int[] findMode(TreeNode root) {
       count = new HashMap<>();
       inorder(root);
       List<Integer> list= new ArrayList<>();
       for (int key: count.keySet()){
            if (count.get(key)==max) list.add(key);
       }
       int [] res= new int[list.size()];
       for (int i=0; i<res.length;i++){
        res[i]=list.get(i);
       }
       return res;
    }

    public void inorder(TreeNode node){
        if (node==null) return;
        inorder(node.left);
        count.put(node.val,count.getOrDefault(node.val,0)+1);
        max=Math.max(max,count.get(node.val));
        inorder(node.right);

    }
}