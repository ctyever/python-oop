class Grade:
    def setGrade(self, kor, eng, math):
        self.first = kor
        self.second = eng
        self.third = math

    def sum(self):
        return (self.first + self.second + self.third)

    def avarage(self):
        return self.sum() / 3


if __name__ == '__main__':
    a = Grade()
    a.setGrade(10, 5, 7)
    print(a.first)
    print(a.sum())
    print(a.avarage())