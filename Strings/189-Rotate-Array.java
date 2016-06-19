/**
 *https://leetcode.com/problems/rotate-array/
 */

public class Solution {
    public void rotate(int[] nums, int k) {
        k %= nums.length;
        
        reverse(nums, 0, nums.length-1); //rotate the whole
        reverse(nums, 0, k-1); //rotate the first half
        reverse(nums, k, nums.length-1); //rotate the 2nd half
    }
    
    public void reverse(int[] nums, int l, int r){
        while (l<r){
            int tmp;
            tmp = nums[r];
            nums[r] = nums[l];
            nums[l] = tmp;
            r--;
            l++;
            
        }
    }
}
