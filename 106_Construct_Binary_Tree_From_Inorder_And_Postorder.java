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
    public TreeNode buildTree(int[] inorder, int[] postorder) {
        if (inorder==null) return null;
        HashMap <Integer,Integer> map = new HashMap <Integer,Integer>();
        for (int i=0;i<inorder.length;i++){
            map.put(inorder[i],i);
        }
        return findRoot(inorder,0,inorder.length-1,postorder,0,postorder.length-1,map);
    }
    
    public TreeNode findRoot(int[] inorder,int is,int ie,int[] postorder,int ps,int pe,HashMap <Integer,Integer> map){
        if (is>ie || ps>pe) return null;
        TreeNode root = new TreeNode(postorder[pe]);
        int index=map.get(postorder[pe]);
        root.left=findRoot(inorder,is,index-1,postorder,ps,index-is+ps-1,map);
        root.right=findRoot(inorder,index+1,ie,postorder,pe-ie+index,pe-1,map);
        return root;
    }
}