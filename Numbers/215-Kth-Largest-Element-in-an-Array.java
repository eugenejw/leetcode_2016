public class Solution {
    public int findKthLargest(int[] nums, int k) {
        int start = 0;
        int last = nums.length - 1;
        int target = nums.length - k;
        int pivot = findPivot(0, last, nums); 
        while (target != pivot){
            if (target < pivot){
                pivot = findPivot(0, pivot-1, nums);
            }else{
                pivot = findPivot(pivot+1, last, nums);
            }
        }
        return nums[target];
        
    }
    
    private int findPivot(int start, int end, int[] nums){
        int pPivot = end;
        int pi = start;
        for (int i = start; i < end; i++){
            if (nums[i] <= nums[pPivot]){
                int tmp = nums[i];
                nums[i] = nums[pi];
                nums[pi] = tmp;
                pi++;
            }
        }
        int tmp = nums[pi];
        nums[pi] = nums[pPivot];
        nums[pPivot] = tmp;
        return pi;
    }
}
