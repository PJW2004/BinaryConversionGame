import random


class Create:

    def __init__(self):
        self.step = {
            1: 100,
            2: 1000,
            3: 100
        }

    def Create_Decimal(self, Max_Decimal=0, User_Answer=0):
        if User_Answer == 3:
            number = random.randint(0, Max_Decimal)
            binary_number = bin(number).replace("0b", "")
            return binary_number
        else:
            number = random.randint(0, Max_Decimal)
            return number

    def Choose_Step(self, User_Answer):
        return self.step[User_Answer]
