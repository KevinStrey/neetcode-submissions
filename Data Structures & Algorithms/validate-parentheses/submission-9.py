class Solution:
    def isValid(self, s: str) -> bool:
        pilha = []
        pares = {'(': ')', '[': ']', '{': '}'}

        for c in s:
            if c in pares:
                pilha.append(c)
            elif not pilha or pares[pilha.pop()] != c:
                return False

        return not pilha