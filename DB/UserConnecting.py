from .db.database import List


class MAIN_CONNECT:
    __MissingCount = 0

    def __init__(self):
        self.State = None
        self.UserName = None
        self.Password = None

    def CONNECT(self, User="", pwd=""):
        self.UserName = User
        self.Password = pwd

        for data in List:
            if data[1] == self.UserName and data[2] == self.Password:
                print("MAIN CONNECTING")
                self.State = "MAIN CONNECTING"
                self.__MissingCount = 0

            elif self.__MissingCount > 2:
                self.State = "Sign Up"

        self.__MissingCount += 1

