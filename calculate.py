class Solution:
    def calculate(self, s: str) -> int:
        stack = []  # Stack to store result and sign
        current_result = 0  # To store the ongoing result
        current_number = 0  # To store the current number
        current_sign = 1  # 1 for '+', -1 for '-'
        
        for char in s:
            if char.isdigit():
                # Build the current number
                current_number = current_number * 10 + int(char)
            
            elif char in '+-':
                # Add the current number to the result with its sign
                current_result += current_sign * current_number
                # Update the current sign (+ or -)
                current_sign = 1 if char == '+' else -1
                # Reset the current number
                current_number = 0
            
            elif char == '(':
                # Push the current result and sign onto the stack
                stack.append(current_result)
                stack.append(current_sign)
                # Reset current result and sign for the new subexpression
                current_result = 0
                current_sign = 1
            
            elif char == ')':
                # Add the current number to the result
                current_result += current_sign * current_number
                # Pop the sign and result from the stack
                current_result *= stack.pop()  # stack.pop() is the sign
                current_result += stack.pop()  # stack.pop() is the previous result
                # Reset the current number
                current_number = 0
        
        # Add the last number to the result
        current_result += current_sign * current_number
        
        return current_result
