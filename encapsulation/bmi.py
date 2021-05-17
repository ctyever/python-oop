class Calbmi():
    def setdata(self, tall, weight):
        self.tall = tall
        self.weight = weight

    def bmi(self):
        return self.weight / (self.tall * self.tall)

    def warning(self):
        if (self.bmi() < 14.33):
            print("low level")
        elif (self.bmi() < 18.24):
            print("normal level")
        else:
            print("high level")

if __name__ == '__main__':
    a = Calbmi()
    a.setdata(1.7, 70)
    print(a.bmi())
    print(a.warning())

