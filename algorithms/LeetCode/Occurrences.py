class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        s = s.lower()
        if 1 <= len(s) <= 1000:
            dec = {}
            for ch in s:
                if ch in dec:
                    dec[ch] += 1
                else:   
                    dec[ch] = 1
            values = dec.values()
            if len(set(values)) == 1:
                return True;
            return False    

        