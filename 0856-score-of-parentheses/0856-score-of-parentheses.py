class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = [0]

        for ch in s:
            if ch == '(':
                stack.append(0)
            else:
                curr = stack.pop()

                if curr == 0:
                    curr = 1
                else:
                    curr = 2 * curr

                stack[-1] += curr

        return stack[0]