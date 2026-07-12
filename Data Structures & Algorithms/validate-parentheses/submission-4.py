class Solution:
    def isValid(self, s: str) -> bool:
        pares = {')': '(', ']': '[', '}': '{'}
        pilha = []

        for c in s:
            if c in pares:
                if not pilha or pilha[-1] != pares[c]:
                    return False
                pilha.pop()
            else:
                pilha.append(c)

        return len(pilha) == 0