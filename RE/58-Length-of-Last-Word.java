//https://leetcode.com/problems/length-of-last-word/
/*
Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.

If the last word does not exist, return 0.

Note: A word is defined as a character sequence consists of non-space characters only.

For example, 
Given s = "Hello World",
return 5.
*/
public class Solution {
    //using java regex
    public int lengthOfLastWord(String s) {
        s = s.trim();
        int lastIndex = s.lastIndexOf(' ')+1;
        //System.out.format("lastIndex is %d \n", lastIndex-1);
        //"a" lastIndex of ' ' will be -1
        return s.length()-lastIndex;
    }
}
