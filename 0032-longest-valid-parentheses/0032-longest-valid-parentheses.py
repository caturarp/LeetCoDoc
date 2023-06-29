class Solution:
    from collections import Counter
    def longestValidParentheses(self, s: str) -> int:
        stack = []
        max_length = 0
        stack.append(-1)  # Push an initial index onto the stack

        for i, c in enumerate(s):
            if c == '(':
                stack.append(i)
            else:
                stack.pop()
                if stack:
                    max_length = max(max_length, i - stack[-1])
                else:
                    stack.append(i)
        return max_length
            