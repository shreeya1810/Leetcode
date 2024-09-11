class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s)!=len(t):
            return False

        map={}

        for i in range(0, len(s)):
            if s[i] in map:
                map[s[i]]+=1
            else:
                map[s[i]]=1
        
        for i in range(0, len(t)):
            if t[i] in map and map[t[i]]!=0 :
                map[t[i]]-=1
            else:
                return False
        return True

        