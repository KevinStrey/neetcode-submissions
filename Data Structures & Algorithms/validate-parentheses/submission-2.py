class Solution:
    def isValid(self, s: str) -> bool:
        fechamento = {')':'(', ']': '[', '}': '{'}
        pilha = []

        for c in s:
            if c in fechamento:
                if not pilha or pilha[-1] != fechamento[c]:
                    return False
                pilha.pop(-1)
            else:
                pilha.append(c)
        if len(pilha) > 0:
            return False
            
        return True

