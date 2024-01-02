from random import randint, choices
class Solution:

    def __init__(self, rects: List[List[int]]):
        self.rects = rects
        self.i = [i for i in range(len(rects))]
        self.weights = [0 for _ in range(len(rects))]
        for i, v in enumerate(rects):
            self.weights[i] = (v[2] - v[0] + 1) * (v[3] - v[1] + 1)
    def pick(self) -> List[int]:
        i = choices(self.i, self.weights , k = 1)
        x1,y1,x2,y2 = self.rects[i[0]]
        return [randint(x1, x2), randint(y1, y2)]
