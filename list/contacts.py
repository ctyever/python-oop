'''
이름, 전화번호, 이메일, 주소를 받아서연락처 입력, 출력, 삭제하는 프로그램을 완성하시오.
'''

class Contacts(object):

    def __init__(self, name, phone, email, adr):
        self.name = name
        self.phone = phone
        self.email = email
        self.adr = adr

    def get_contacts(self):
        return f'이름 : {self.name} 전화번호 : {self.phone} 이메일 : {self.email} 주소 : {self.adr}'

    @staticmethod
    def main():

        ls = []

        while 1:

            menu = int(input("1. 주소록 추가\n0. 프로그램 종료\n2. 출력"))

            if menu == 0:
                break

            elif menu == 1:
                ls.append(Contacts(input('이름 : '), input('전화번호 : '), input('이메일 : '), input('주소 : ')))

            elif menu == 2:
                for i in ls:
                    print(f'출력결과 : {i.get_contacts()}')
            else:
                print("잘못된 주문입니다")
                continue

Contacts.main()


