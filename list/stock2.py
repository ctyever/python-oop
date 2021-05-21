class Stock2(object):

    def __init__(self, name, code):
        self.name = name
        self.code = code

    def to_string(self):
        return f'종목명 : {self.name} 코드 : {self.code}'

    @staticmethod
    def del_account(ls, code):
        for i, j in enumerate(ls):
            if j.name == code:
                del ls[i]

    @staticmethod
    def main():

        ls = []

        while 1:
            menu = input("0.프로그램 종료\n1.종목입력\n2.출력\n3.수정\n4.삭제")


            if menu == '0':
                break
            elif menu == '1':
                ls.append(Stock2(input("종목명 : "), input("코드 : ")))
            elif menu == '2':
                for i in ls:
                    print(i.to_string())
            elif menu == '3':
                code = input("수정할 코드: ")
                stock = Stock2(input("종목명 : "), code)
                stock.del_account(ls, code)
                ls.append(stock)
            elif menu == '4':
                stock = Stock2(None, input("삭제할 코드: "))
                stock.del_account(ls, stock.code)
            else:
                print("잘못된 번호입니다")
                continue

Stock2.main()