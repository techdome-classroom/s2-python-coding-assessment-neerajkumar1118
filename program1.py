class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # Dictionary to store matching pairs of brackets
        bracket_map = {')': '(', '}': '{', ']': '['}
        
        # Stack to keep track of opening brackets
        stack = []
        
        # Iterate over each character in the string
        for char in s:
            if char in bracket_map.values():
                # If it's an opening bracket, push it to the stack
                stack.append(char)
            elif char in bracket_map.keys():
                # If it's a closing bracket, check for matching opening bracket
                if not stack or stack[-1] != bracket_map[char]:
                    return False  # If no match, return False
                stack.pop()  # Pop the matching opening bracket from the stack
        
        # If the stack is empty, all brackets are matched
        return len(stack) == 0








    



  

