import math

class Calbmi(object):

    def __init__(self, tall, weight):
        self.tall = tall
        self.weight = weight

    def get_bmi(self):
        bmi = self.weight / self.tall ** 2 * 10000

        if bmi < 18.5:
            bb =  "low level"
        elif bmi < 23:
            bb = "normal level"
        elif bmi < 25:
            bb = "high level"
        else:
            bb = "bboom"

        return f'나의 bmi는 {int(bmi)}, {bb}'

    @staticmethod
    def main():
        bmi = Calbmi(int(input("나의 키 : ")), int(input("나의 몸무게 : ")))
        print(bmi.get_bmi())


Calbmi.main()







