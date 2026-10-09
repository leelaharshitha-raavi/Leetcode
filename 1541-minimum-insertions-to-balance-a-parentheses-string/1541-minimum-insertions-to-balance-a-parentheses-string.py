class Solution:
    def minInsertions(self, s):
        open = 0
        ans = 0
        i = 0

        while i < len(s):
            if s[i] == '(':
                open += 1
                i += 1

            else:
                # We need two consecutive ')'
                if i + 1 < len(s) and s[i + 1] == ')':
                    i += 2
                else:
                    # Insert one ')' to make '))'
                    ans += 1
                    i += 1

                # Match the closing pair with an opening '('
                if open > 0:
                    open -= 1
                else:
                    # No opening '(' available; insert one
                    ans += 1

        # Every remaining '(' needs two ')'
        ans += open * 2

        return ans