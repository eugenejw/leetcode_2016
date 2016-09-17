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
     * @link https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/
     * 
     */
    public TreeNode buildTree(int[] inorder, int[] postorder) {
        TreeNode root = buildTree(inorder, 0, inorder.length-1, postorder, 0, postorder.length-1);
        return root;
        
    }
    
    public TreeNode buildTree(int[] inorder, int ins, int ine, int[] postorder, int pos, int poe) {
        if(ins > ine || pos > poe) return null;

        TreeNode root = new TreeNode(postorder[poe]);
        int pivot = ins;
        for (int i=ins; i<=ine; i++) {
            if(inorder[i] == postorder[poe]) {
                pivot = i; 
                break;
            }
        }
        int leftTreeLength = pivot - ins;
        root.left = buildTree(inorder, ins, pivot-1, postorder, pos, pos+leftTreeLength-1);
        root.right = buildTree(inorder, pivot+1, ine, postorder, pos+leftTreeLength, poe-1);
        return root;
    }
}
