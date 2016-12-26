/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
public class Solution {   //too many calling rob() time exceed!!!!!!!!
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
        int left;
        int right;
        if (root==null) return 0;
        if ((root.left==null) && (root.right==null) )
            return root.val;
        if (root.left!=null)
            left=rob(root.left.left)+rob(root.left.right);
        else left=0;
        if (root.right!=null)
            right=rob(root.right.left)+rob(root.right.right);
        else right=0;
        int l=rob(root.left);
        int r=rob(root.right);
        if ((root.val+left+right)>(l+r))
            return root.val+left+right;
        else 
            return l+r;
    }
}

/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
public class Solution {  //res[0] wightout the current node; res[0] using the current node
    public int rob(TreeNode root) {
        int[] result=dfs(root);
        return Math.max(result[0],result[1]);
    }
    public int[] dfs(TreeNode node){
        int[] res=new int[2];
        if (node==null)
         return res;
     int [] left=dfs(node.left);
     int [] right=dfs(node.right);
     res[0]=Math.max(left[0],left[1])+Math.max(right[0],right[1]);
     res[1]=left[0]+right[0]+node.val;
     return res;
 }
}





