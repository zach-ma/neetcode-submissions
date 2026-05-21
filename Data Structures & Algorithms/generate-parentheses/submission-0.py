class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def recurse(opening, closing, cur):
            if opening == n and closing == n:
                res.append(''.join(cur.copy()))
                return
            if opening < n:
                cur.append('(')
                recurse(opening+1, closing, cur)
                cur.pop()
            if opening > closing:
                cur.append(')')
                recurse(opening, closing+1, cur)
                cur.pop()
            
        recurse(0, 0, [])
        return res

