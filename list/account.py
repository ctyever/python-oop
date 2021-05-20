import random

class Account(object):

    def __init__(self, name, money):
        self.bankname = "sc은행"
        self.name = name
        self.money = money
        self.accontnum = random.random() * 1000

    def get_info(self):
        return f'이름 : {self.name} 잔액 : {self.money} 은행 : {self.bankname} 계좌 번호 : {self.accontnum}'

    @staticmethod
    def main():
        ls = []
        while 1:
            menu = input("0.프로그램 종료\n1. 정보 입력\n2.출력\n3.삭제\n4.수정")

            if menu == '0':
                break
            elif menu == '1':
                ls.append(Account(input("이름"), input("잔액")))
            elif menu == '2':
                for i in ls:
                    print(i.get_info())
            elif menu == '3':
                del_info = input("삭제할 이름 : ")
                for i, j in enumerate(ls):
                    if j.name == del_info:
                        del ls[i]
            elif menu == '4':
                edit_name = input("수정할 이름 : ")
                edit_info = Account(edit_name, input("잔액"))
                for i, j in enumerate(ls):
                    if j.name == edit_name:
                        del ls[i]
                        ls.append(edit_info)


            else:
                print("잘못된 주문입니다")

Account.main()






