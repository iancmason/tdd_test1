class Stock:
    def __init__(self,symbol):
        self.symbol = symbol
        self.price = None

    def update(self,timestamp,price):
        if price < 0:
            raise ValueError("price should not be negative")
        self.price_history.append(price)

    @property
    def price(self):
        return self.price_history[-3] < \
        self.price_history[-2] < self.price_history[-1]

if __name__ == "__main__":
    unittest.main()
