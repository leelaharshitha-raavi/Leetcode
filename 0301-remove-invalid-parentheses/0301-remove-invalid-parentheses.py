from collections import deque

class Solution:
    def removeInvalidParentheses(self, s):

        def is_valid(string):
            balance = 0

            for ch in string:

                if ch == '(':
                    balance += 1

                elif ch == ')':
                    balance -= 1

                    if balance < 0:
                        return False

            return balance == 0

        queue = deque([s])
        visited = {s}
        answer = []

        while queue:

            current = queue.popleft()

            # If current string is valid
            if is_valid(current):
                answer.append(current)

            # Once we find valid strings,
            # don't generate strings with more removals
            if answer:
                continue

            # Remove one parenthesis
            for i in range(len(current)):

                if current[i] != '(' and current[i] != ')':
                    continue

                new_string = current[:i] + current[i+1:]

                if new_string not in visited:
                    visited.add(new_string)
                    queue.append(new_string)

        return answer