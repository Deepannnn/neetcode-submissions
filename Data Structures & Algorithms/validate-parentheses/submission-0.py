class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]

        for i in s:
            if i=='(' or i=='{' or i=='[':
                stack.append(i)
            else:
                if not stack :
                    return False
                n=stack.pop()
                if i==')' and n=='(':
                    continue
                elif i=='}' and n=='{':
                    continue
                elif i==']' and n=='[':
                    continue
                else:
                    return False
        return len(stack)==0                     