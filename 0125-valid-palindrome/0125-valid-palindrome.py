class Solution:
    def isPalindrome(self, s: str) -> bool:

        pattern = r'[^A-Za-z0-9]+'
        s = re.sub(pattern, '', s)
        s=s.strip().lower()
        t=s
        t=list(t)
        s=list(s)

        i=0
        j=len(s)-1

        while i<j:
            s[i], s[j] = s[j], s[i]
            i+=1
            j-=1
        if s==t:
            return True
        return False

        
        