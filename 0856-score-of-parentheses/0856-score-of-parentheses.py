class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        st=[0]
        for ch in s:
            if ch=="(":
                st.append(0)
            else:
                cur=st.pop()
                if cur==0:
                    cur=1
                else:
                    cur=2*cur
                st[-1]+=cur
        return st[0]