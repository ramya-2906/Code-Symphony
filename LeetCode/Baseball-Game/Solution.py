class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        
        for op in operations:
            # Case 1: number (can be negative)
            if op.lstrip('-').isdigit():
                stack.append(int(op))
            
            # Case 2: "C" → remove last score
            elif op == "C":
                stack.pop()
            
            # Case 3: "D" → double last score
            elif op == "D":
                stack.append(2 * stack[-1])
            
            # Case 4: "+" → sum of last two scores
            elif op == "+":
                stack.append(stack[-1] + stack[-2])
        
        # Final total score
        return sum(stack)