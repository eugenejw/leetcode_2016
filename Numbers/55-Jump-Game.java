public class Solution {
    /*
    *@link https://leetcode.com/problems/jump-game/
    */
    public boolean canJump(int[] nums) {
        int n = nums.length;
        int last = n-1;
        for (int i=n-2; i>=0; i--){
            if (nums[i]+i >= last){
                last = i;
                //System.out.println("last: "+last);
            }
        }
        return last==0;
    }
}
