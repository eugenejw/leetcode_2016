ublic class Solution {
    public boolean isValid(String s) {
        char[] ch = s.toCharArray();
        Stack<Character> stack = new Stack<Character>();
        HashMap d = new HashMap();
        d.put(')', '(');
        d.put(']', '[');
        d.put('}', '{');
        
        for(char e: ch){
            if (e=='{' || e=='[' || e=='('){
                stack.push(e);
            }else{
                if (stack.isEmpty()){
                    return false;
                }
                if (d.get(e) == stack.peek()){
                    stack.pop();
                }else{
                    return false;
                }
                
            }
        }
        if (stack.isEmpty()){
            return true;
        }else{
            return false;
        }
        
    }
}
