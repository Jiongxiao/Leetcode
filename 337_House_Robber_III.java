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
    public int rob(TreeNode root) {
        Solution s=new Solution();
        int left;
        int right;
        if (root==null) return 0;
        if ((root.left==null) && (root.right==null) )
            return root.val;
        if (root.left!=null)
            left=s.rob(root.left.left)+s.rob(root.left.right);
        else left=0;
        if (root.right!=null)
            right=s.rob(root.right.left)+s.rob(root.right.right);
        else right=0;
        if ((root.val+left+right)>(s.rob(root.left)+s.rob(root.right)))
            return root.val+left+right;
        else 
            return s.rob(root.left)+s.rob(root.right);
    }
}
