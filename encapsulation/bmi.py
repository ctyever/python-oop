import math

class Calbmi(object):

    def __init__(self, tall, weight):
        self.tall = tall
        self.weight = weight

    def get_bmi(self):
        return self.weight / self.tall ** 2 * 10000

    def warning(self):
        if self.get_bmi() < 18.5:
            return "low level"
        elif self.get_bmi() < 23:
            return "normal level"
        elif self.get_bmi() < 25:
            return "high level"
        else:
            return "bboom"

    @staticmethod
    def main():
        bmi = Calbmi(int(input("나의 키 : ")), int(input("나의 몸무게 : ")))
        print(f'나의 bmi는 {math.floor(bmi.get_bmi())} 입니다. 나의 비만도는 {bmi.warning()} 입니다')



Calbmi.main()







