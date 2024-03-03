class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        res=[0]*len(temperatures)

        stack=[]

        for key,value in enumerate(temperatures):

            # popping elements until the top of stack is greater then the current element

            while stack and stack[-1][0]< value:
                res[stack[-1][1]]=key-stack[-1][1]
                stack.pop()

            stack.append([value,key])

        return res
