class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        short_term = list(s) if len(s) < len(t) else list(t)
        long_term  = list(t) if len(s) < len(t) else list(s)
        
        if len(long_term) == len(short_term):
            for i in range(len(long_term)):
                if short_term[i] != long_term[i]:
                    short_term[i] = long_term[i]
                    return short_term == long_term
            
        if len(long_term) == len(short_term) + 1:
            for i in range(len(long_term)):
                try:
                    if short_term[i] != long_term[i]:
                        short_term.insert(i, long_term[i])
                except:
                    if i == 0:
                        short_term = long_term
                    elif i == len(short_term) - 1:
                        short_term.append(long_term[i])
                    else:
                        short_term.insert(i, long_term[i])
            return short_term == long_term
        return False        