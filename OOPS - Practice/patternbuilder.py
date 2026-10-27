class PatternBuilder:
    def __init__(self, symbol, size):
        self.symbol = symbol
        self.size = size

    def draw_hollow_square(self):
        for i in range(self.size):
            for j in range(self.size):
                if i == 0 or j == 0 or i == self.size - 1 or j == self.size - 1:
                    print(self.symbol, end="")
                else:
                    print(" ", end="")
            print(f"\n")

pat = PatternBuilder("*", 4)
pat.draw_hollow_square()

