//https://leetcode.com/problems/reverse-bits/
/*
Reverse bits of a given 32 bits unsigned integer.

For example, given input 43261596 (represented in binary as 00000010100101000001111010011100), return 964176192 (represented in binary as 00111001011110000010100101000000).

Follow up:
If this function is called many times, how would you optimize it?
 */

public class Solution {
    // you need treat n as an unsigned value
    //https://leetcode.com/discuss/77219/2ms-java-solutionx
    public int reverseBits(int n) {
        int res = 0;
        for (int i=0; i<32; i++){
            //make space for res
            res = res << 1;
            //get the last binary digit of n
            int lastDigit = (n>>i)&1;
            //set the last digit of res
            res |= lastDigit;
            
            
        }
        return res;
    }
}
