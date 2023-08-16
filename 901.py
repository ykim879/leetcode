class StockSpanner:

    def __init__(self):
        self.hist = [] #stack the (stock_price, span)
    def next(self, price: int) -> int:
        res = 1
        while self.hist and self.hist[-1][0] <= price:
            res += self.hist.pop()[1]
        self.hist.append((price, res))
        return res
