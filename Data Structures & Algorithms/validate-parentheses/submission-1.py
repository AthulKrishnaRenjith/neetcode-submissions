class Solution:
    def isValid(self, s: str) -> bool:
        k = []
        for i in range(len(s)):
            if s[i] in ('(', '{','['):
                k.append(s[i])
            elif s[i] in (')'):
                if len(k) != 0 and k[len(k) - 1] in ('(') :
                    k.pop()
                else:
                    return False
            elif s[i] in ('}'):
                if len(k) != 0 and k[len(k) - 1] in ('{'):
                    k.pop()
                else:
                    return False
            elif s[i] in (']'):
                if len(k) != 0 and k[len(k) - 1] in ('['):
                    k.pop()
                else:
                    return False
        if len(s) == 0:
            return False
        elif len(k) == 0:
            return True
        else:
            return False