class Conversion:

    def Decimal_To_Binary(self, Decimal):
        Binary = bin(Decimal).replace("0b", "")
        return Binary

    def test(self, Answer=''):
        User_Answer = input(">>")
        if Answer == User_Answer:
            print("정답\n")
        else:
            self.test(Answer)
