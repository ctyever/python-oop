class Grade:

    def __init__(self, kor, eng, math):
        self.kor = kor
        self.eng = eng
        self.math = math

    def sum(self):
        return (self.kor + self.eng + self.math)

    def avarage(self):
        return self.sum() / 3

    def get_grade(self):
        score = int(self.avarage())
        #grade = ''
        if score >= 90:
            grade = 'A학점'
        elif score >= 80:
            grade = 'B학점'
        elif score >= 70:
            grade = 'C학점'
        else:
            grade = 'D학점'

        return grade


    @staticmethod
    def main():
        a = Grade(int(input("국어점수입력")), int(input("영어점수입력")), int(input("수학점수입력")))
        print(f'총 점수 : {a.sum()}')
        print(f'평균 점수 : {a.avarage()}')
        print(f'학점 : {a.get_grade()}')


Grade.main()
