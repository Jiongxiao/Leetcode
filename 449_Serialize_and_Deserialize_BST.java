/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
public class Codec {

    // Encodes a tree to a single string.
    private static final String sep=",";
    public String serialize(TreeNode root) { // preorder
        if (root==null) return "null";
        Stack <TreeNode>st= new Stack<>();
        StringBuilder sb= new StringBuilder();
        st.push(root);
        while(!st.empty()){
            root=st.pop();
            sb.append(root.val).append(sep);
            if (root.right != null) st.push(root.right);
            if (root.left != null) st.push(root.left);
        }
        return sb.toString();
    }

    // Decodes your encoded data to tree.
    public TreeNode deserialize(String data) { // sort preorder to get inorder
        if (data.equals("null")) return null;
        String [] strs= data.split(sep);
        int [] pre= new int[strs.length];
        int [] in= new int[strs.length];
        for (int i =0; i<strs.length; i++){
            pre[i]=Integer.parseInt(strs[i]);
        }
        in=pre.clone();
        Arrays.sort(in);
        return buildTree(pre,in);
    }

    public TreeNode buildTree(int[] pre, int[] in){  //build tree from inorder and preorder 
        HashMap <Integer,Integer> map=new HashMap<>();
        for (int i=0; i< in.length; i++){
            map.put(in[i],i);
        }
        return findRoot(pre,0,pre.length-1,in,0,in.length-1,map);
    }

    TreeNode findRoot(int[] pre, int ps, int pe, int[] in, int is, int ie,
     HashMap <Integer, Integer>map){
        if (is>ie || ps>pe) return null;
        // System.out.println(ps);
        TreeNode root= new TreeNode(pre[ps]);
        int index=map.get(pre[ps]);
        root.left=findRoot(pre,ps+1,ps+index-is,in, is, index-1,map);
        root.right=findRoot(pre,ps+index-is+1,pe, in, index+1,ie, map);
        return root;
    }
}

// Your Codec object will be instantiated and called as such:
// Codec codec = new Codec();
// codec.deserialize(codec.serialize(root));