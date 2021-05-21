import random

class Account(object):

    def __init__(self, accountnum, name, money):
        self.BANK_NAME = "SC은행"
        self.name = name
        self.money = money
        self.accountnum = accountnum

    '''
       계좌번호는 3자리-2자리-6자리 형태로 랜덤하게 생성됩니다.
    '''
    
    def to_string(self):
        return f'이름 : {self.name} 잔액 : {self.money} 은행 : {self.BANK_NAME} 계좌 번호 : {self.accountnum}'

    @staticmethod
    def create_accountnum():
        ls = [str(random.randint(0, 9)) for i in range(3)]
        ls.append(('-'))
        for i in range(2):
            ls.append(str(random.randint(0, 9)))
        ls.append(('-'))
        for i in range(6):
            ls.append(str(random.randint(0, 9)))
        return "".join(ls)

    @staticmethod
    def del_account(ls, account_number):
        for i, j in enumerate(ls):
            if j.accountnum == account_number:
                del ls[i]

    @staticmethod
    def replace(ls, account_number, money, menu):
        for i, j in enumerate(ls):
            if j.accountnum == account_number:
                Account.del_account(ls, account_number)
                if menu == '3':
                    replace = Account(j.accountnum,
                                      j.name,
                                      int(j.money) + int(money))
                    ls.append(replace)
                elif menu == '4':
                    replace = Account(j.accountnum,
                                      j.name,
                                      int(j.money) - int(money))
                    ls.append(replace)
    @staticmethod
    def main():
        ls = []
        while 1:
            menu = input("0.종료 1.계좌계설 2.계좌목록 3.입금 4.출금 5.계좌탈퇴")

            if menu == '0':
                break
            elif menu == '1':
                ls.append(Account(Account.create_accountnum(), input("이름"), input("잔액")))
            elif menu == '2':
                for i in ls:
                    print(i.to_string())
            elif menu == '3':
                account_number = input("계좌 번호 : ")
                money = input('입금액 입력 바랍니다')
                Account.replace(ls, account_number,money, menu)

            elif menu == '4':
                account_number = input("계좌 번호 : ")
                money = input('출금액 입력 바랍니다')
                Account.replace(ls, account_number, money, menu)
            elif menu == '5':
                Account.del_account(ls, input("계좌 번호 : "))
            else:
                print("잘못된 주문입니다")
                continue

Account.main()








