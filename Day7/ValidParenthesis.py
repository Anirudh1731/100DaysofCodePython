class Solution:
    def isValid(self, s: str) -> bool:

        stack=[]

        hashmap={")":"(" , "}":"{", "]":"["}

        for i in s:
            if i in hashmap:
                if stack and hashmap[i]==stack[-1]:
                    stack.pop()
                else:
                    return False
            
            else:
                stack.append(i)

        return True if not stack else False
        
