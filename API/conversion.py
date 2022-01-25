class Conversion:

    def Decimal_To_Binary(self, Decimal, User_Answer=0):
        if User_Answer == 3:
            return int(Decimal, 2)

        else:
            Binary = bin(Decimal).replace("0b", "")
            return Binary

    def test(self, Answer=''):
        User_Answer = input(">>")
        if f'{Answer}' == User_Answer:
            print("정답\n")
        else:
            self.test(Answer)
