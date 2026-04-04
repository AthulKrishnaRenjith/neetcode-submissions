class Solution:
    def isValid(self, s: str) -> bool:
        k = []
        matching = {")": "(", "}": "{", "]": "["}
        for i in range(len(s)):
            if s[i] in ('(', '{','['):
                k.append(s[i])
            elif len(k) != 0 and matching[s[i]] == k[-1]:
                k.pop()
            else:
                return False
        return len(k) == 0