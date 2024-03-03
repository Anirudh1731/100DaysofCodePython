class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        stack=[]
        res=[]

        #open should be less than close

        def backtrack(open,close):

            if(open==close==n):
                res.append("".join(stack))

            
            if open<n:
                stack.append('(')
                backtrack(open+1,close)

                stack.pop()

            if close < open:

                stack.append(')')
                backtrack(open,close+1)
                stack.pop()

            
        backtrack(0,0)
        return res
        
