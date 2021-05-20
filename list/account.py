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
            menu = input("1. 정보 입력\n2.출력\n0.프로그램 종료\n3.삭제\n4.수정")

            if menu == '0':
                break
            elif menu == '1':
                ls.append(Account(input("이름"), input("잔액")))
            elif menu == '2':
                for i in ls:
                    print(i.get_info())
            elif menu == '3':
                del_name = input("삭제할 이름 : ")
                for i, j in enumerate(ls):
                    if j.name == del_name:
                        del ls[i]

            else:
                print("잘못된 주문입니다")

Account.main()






