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
    def del_account(ls, name):
        for i, j in enumerate(ls):
            if j.name == name:
                del ls[i]

    @staticmethod
    def main():

        ls = []

        while 1:

            menu = int(input("0. 프로그램 종료\n1. 주소록 추가\n2. 출력\n3.수정\n4.삭제"))

            if menu == 0:
                break

            elif menu == 1:
                ls.append(Contacts(input('이름 : '), input('전화번호 : '), input('이메일 : '), input('주소 : ')))

            elif menu == 2:
                for i in ls:
                    print(f'출력결과 : {i.get_contacts()}')
            elif menu == 3:
                edit_name = input("수정할 이름 : ")
                edit_info = Contacts(edit_name, input('수정 전화번호 : '), input('수정 이메일 : '), input('수정 주소 : '))
                edit_info.del_account(ls, edit_name)
                ls.append(edit_info)
            elif menu == 4:
                del_name = input("삭제할 이름 : ")
                name = Contacts(del_name, None, None, None)
                name.del_account(ls, del_name)

            else:
                print("잘못된 주문입니다")
                continue

Contacts.main()


