def add_function(first, second):
    return first + second

def sub_function(first, second):
    return first - second

def mul_function(first, second):
    return first * second

def div_function(first, second):
    return first / second


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
    #c = Calculator()
    #c.setdata(3, 1)
    #print(c.sub())
    print(add_function(3, 1))
    print(sub_function(3, 1))
    print(mul_function(3, 1))
    print(div_function(3, 1))