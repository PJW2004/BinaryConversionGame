class MAIN_CONNECT:
    __MissingCount = 0

    def __init__(self):
        self.State = None
        self.UserName = None
        self.Password = None

    def CONNECT(self, User="", pwd=""):
        self.UserName = User
        self.Password = pwd

        with open("./DB/USER_DB", "r") as Userdata:
            # Connect 과정
            for data in Userdata:
                if data.split(':')[0] == self.UserName and data.split(':')[1][:-2] == self.Password:
                    print("MAIN CONNECTING")
                    self.State = "MAIN CONNECTING"
                    self.__MissingCount -= 1

                elif self.__MissingCount > 2:
                    self.State = "Sign Up"

            self.__MissingCount += 1

            Userdata.close()

