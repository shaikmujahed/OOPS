class Decimal:
    def __init__(self,number,place):
        self.number = number
        self.place = place
    def __repr__(self):
        return "%.{}f".format(self.place) % self.number


class Currency(Decimal):
    def __init__(self,symbol,number,place):
        super().__init__(number, place)
        self.symbol = symbol

    def __repr__(self):
        return "{}{}".format(self.symbol,super().__repr__())


print(Decimal(11.3256,2))
print(Currency("$",15.4565,3))


