class Solution:
    def isValid(self, s: str) -> bool:
        
        stck = []

        dic = {')':'(', '}':'{', ']':'['}

        for i in s:
            if i in dic:
                if stck and stck[-1] == dic[i]:
                    stck.pop()
                else:
                    return False
            else:
                stck.append(i)
        
        return True if not stck else False



        


        


            

            
            