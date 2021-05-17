class Calculator:
    def setdata(self, first, second):
        self.first = first
        self.second = second

    def add(self):
        return self.first + self.second

    def sub(self):
        return self.first - self.second

    def mul(self):
        return self.first * self.second

    def div(self):
        return self.first / self.second

if __name__ == '__main__':
    c = Calculator()
    c.setdata(3, 1)
    print(c.sub())