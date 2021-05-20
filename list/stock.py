class Stock(object):

    def __init__(self, name, code):
        self.name = name
        self.code = code

    def get_stock(self):
        return f'종목명 : {self.name}, 종목코드 : {self.code}'

    @staticmethod
    def main():

        while 1:
            menu = int(input("1.종목 저장\n2.출력\n0.프로그램 종료\n"))

            if menu == 0:
                break
            elif menu == 1:
                s = Stock(input("종목명 : "), input("종목 코드 : "))
            elif menu == 2:
                print(s.get_stock())
            else:
                print("잘못된 주문입니다")
                continue

Stock.main()
