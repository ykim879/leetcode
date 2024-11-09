directions = {"R": (0, 1), "L" : (0, -1), "D" : (1, 0), "U" : (-1,0)}
class SnakeGame:
    def __init__(self, width: int, height: int, food: List[List[int]]):
        self.width = width
        self.height = height
        self.foods = food
        self.foods.append([-1,-1])
        self.i = 0
        self.score = 0
        self.bodyset = {(0,0)}
        self.bodyq = deque([(0,0)]) # where this current snack

    def move(self, direction: str) -> int:
        # if new direction is in set or out of bound: return -1
        delta, head = directions[direction], self.bodyq[0]
        r, c = delta[0] + head[0], delta[1] + head[1]
        if not (0 <= r < self.height) or not (0 <= c < self.width) or ((r,c) in self.bodyset and (r,c) != self.bodyq[-1]):
            return -1
        # if it is food: new direction will append to front and in the set
        food = self.foods[self.i]
        if r == food[0] and c == food[1]:
            self.score += 1
            self.i += 1 # does food ever go out of bound?
        # if it is not food body will append on front new direction on front (add this on set) and popped at back (remove this on set)
        else:
            l = self.bodyq.pop()
            self.bodyset.remove(l)
        self.bodyset.add((r,c))
        self.bodyq.appendleft((r,c))
        return self.score


# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)
