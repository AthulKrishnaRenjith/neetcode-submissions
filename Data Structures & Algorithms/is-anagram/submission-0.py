class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seen = {}
        heard = {}
        for i in s:
            if i in seen:
                seen[i]+=1
            else:
                seen[i]=1
        for j in t:
            if j in heard:
                heard[j]+=1
            else:
                heard[j]=1
        if seen == heard:
            return True
        else:
            return False

        