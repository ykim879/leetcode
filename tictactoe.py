class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        count = Counter()
        for i, move in enumerate(moves):
            r, c = move
            score = 1
            if i % 2:
                score = -1
            count[r] += score
            count[c+3] += score
            if r == c:
                count[6] += score
            if r == 2 - c:
                count[7] += score
        for c in count.values():
            if c == 3:
                return "A"
            elif c == -3:
                return "B"
        return "Draw" if len(moves) == 9 else "Pending"
