class Solution:
    def minMovesToCaptureTheQueen(self, a: int, b: int, c: int, d: int, e: int, f: int) -> int:
        if (a == e and not (a == c and d >= min(b,f) and d <= max(b,f))) or (b == f and not (d == f and c >= min(a,e) and c <= max(a,e))) or (abs(e-c) == abs(f-d) and not(abs(a-e) == abs(b-f) and (abs(a-c) == abs(b-d))and min(c,e) <= a and e <= max(c,e) and min(d,f) <= b and b <= max(d,f))):
            return 1
        return 2
        
