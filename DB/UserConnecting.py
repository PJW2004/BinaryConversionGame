class MAIN_CONNECT:
    def __init__(self, UserName="", Password=""):
        with open("./DB/USER_DB", "r") as Userdata:
            for data in Userdata:
                if data.split(':')[0] == UserName and data.split(':')[1][:-2] == Password:
                    print("MAIN CONNECTING")
                    self.State = "MAIN CONNECTING"

                else:
                    print("SORRY INFORMATION DOSE NOT EXIST")
                    self.State = "SORRY INFORMATION DOSE NOT EXIST"

