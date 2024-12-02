class Solution:
    def compress(self, chars: List[str]) -> int:
        def alignCount(ins, count):
            for i, c in enumerate(str(count)):
                chars[ins] = c
                ins += 1
            return ins
        ins,count = 1, 1
        for i in range(1, len(chars)):
            if chars[i - 1] == chars[i]:
                count += 1
            else:
                if count > 1:
                    ins = alignCount(ins, count)
                chars[ins] = chars[i]
                ins += 1
                count = 1
        if count > 1:
            ins = alignCount(ins, count)
        return ins
