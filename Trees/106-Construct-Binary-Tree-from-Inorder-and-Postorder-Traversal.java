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
    /**
     * @see https://discuss.leetcode.com/topic/3296/my-recursive-java-code-with-o-n-time-and-o-n-space/2
     */
    public TreeNode buildTree(int[] inorder, int[] postorder) {
        if (inorder == null || postorder == null || inorder.length != postorder.length) return null;
        HashMap<Integer, Integer> hm = new HashMap<Integer,Integer>();
        for (int i=0; i<inorder.length; i++){
            hm.put(inorder[i], i);
        }
        return buildTree(inorder, postorder, 0, inorder.length-1, 0, postorder.length-1, hm);
    }
    
    public TreeNode buildTree(int[] inorder, int[] postorder, int is, int ie, int ps, int pe, HashMap<Integer,Integer> hm) {
        if (ps > pe || is > ie){
            return null;
        }
        TreeNode root = new TreeNode(postorder[pe]);
        int pivot = hm.get(postorder[pe]);
        TreeNode leftNode = buildTree(inorder, postorder, is, pivot-1, ps, ps+pivot-is-1 , hm);
        TreeNode rightNode = buildTree(inorder, postorder, pivot+1, ie, ps+pivot-is, pe-1 , hm);
        root.left = leftNode;
        root.right = rightNode;
        return root;
        
    }
}
