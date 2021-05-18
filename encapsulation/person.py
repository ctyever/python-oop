'''
이름, 출생년도, 주소를 입력받아서
회원 가입한 사람의 이름, 나이 , 주소를 출력하시오
'''
class Person(object):

    def __init__(self, name, bir, adr):
        self.name = name
        self.bir = bir
        self.adr = adr

    @staticmethod
    def main():
        p = Person(input("이름 : "), input("출생년도 : "), input("주소 : "))



if __name__ == '__main__':
    pass