import os.path


class MAIN_Start:
    def __init__(self):
        if not os.path.exists("./DB/USER_DB"):
            with open("./DB/USER_DB", "w") as Userdata:
                Userdata.write(f"admin:admin123,\n")
                Userdata.close()

    def SignUPAnswer(self):
        UserAnswer = input("Do you Want to Sign Up?")
        if UserAnswer == "YES" or UserAnswer == "Y":
            return "Y"
        elif UserAnswer == "NO" or UserAnswer == "N":
            pass
        else:
            print("Please answer is YES/Y OR NO/N\n")
            self.SignUPAnswer()

    def SignUp(self):
        UserName = input("PLEASE WRITE YOUR USERNAME")
        password = input("PLEASE WRITE YOUR PASSWORD")

        with open("./DB/USER_DB", "a") as Userdata:
            Userdata.write(f"{UserName}:{password},\n")
            Userdata.close()