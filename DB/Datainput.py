import os.path


class MAIN_Start:
    def __init__(self):
        self.memory = ""
        if not os.path.exists("./DB/USER_DB"):
            with open("./DB/USER_DB", "w") as Userdata:
                Userdata.write(f"admin:admin123,\n")
                Userdata.close()

        self.CreateDB(DBNAME="LOG")
        self.CreateDB(DBNAME="USER_LOG")

    def CreateDB(self, DBNAME=""):
        if not os.path.exists(f"./DB/{DBNAME}"):
            with open(f"./DB/{DBNAME}", "w") as LOG:
                LOG.write("")
                LOG.close()

    def InputLOG(self, DBNAME="", HEAD="", LOG=""):
        with open(f"./DB/{DBNAME}", "a") as DB:
            DB.write(f"{HEAD}:{LOG},\n")
            DB.close()

    def SignUPAnswer(self):
        UserAnswer = input("Do you Want to Sign Up?\n>>")
        if UserAnswer == "YES" or UserAnswer == "Y":
            return "Y"
        elif UserAnswer == "NO" or UserAnswer == "N":
            pass
        else:
            print("Please answer is YES/Y OR NO/N\n")
            self.SignUPAnswer()

    def SignUp(self):
        UserName = input("PLEASE WRITE YOUR USERNAME : ")

        if UserName == "admin":
            print("[경고] 'admin' 은 만들 수 없습니다.")

        else:
            password = input("PLEASE WRITE YOUR PASSWORD : ")

            with open("./DB/USER_DB", "a") as Userdata:
                Userdata.write(f"{UserName}:{password},\n")
                Userdata.close()

    def withdrawal(self):
        UserName = input("PLEASE WRITE YOUR WANT DELETE DELETE USERNAME\n>>")

        if UserName == "admin":
            print("[경고] 'admin' 은 지울 수 없습니다.")
            print("END THE PROGRAM")

        else:
            with open("./DB/USER_DB", "r") as Userdata:
                for data in Userdata:
                    print(data)
                    Name = data.split(":")[0]

                    if Name != UserName:
                        Password = data.split(":")[1][:-2]
                        print(Password)
                        self.memory += f"{Name}:{Password},\n"
                Userdata.close()

            self.reloading()

    def reloading(self):
        print(self.memory)
        with open("./DB/USER_DB", "w") as Userdata:
            Userdata.write(self.memory)
            Userdata.close()

        print("DELETE SUCCESS")