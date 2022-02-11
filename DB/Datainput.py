from .db.database import Session, engine, Base
from .db import models

Base.metadata.create_all(engine)


class MAIN_Start:
    def __init__(self):
        self.memory = ""
        self.db = Session()

    def InputLOG(self, Step="", User="", LOG=""):
        new_LOG = models.LOG(User=User, Step=Step, time=LOG)
        self.db.add(new_LOG)
        self.db.commit()
        self.db.refresh(new_LOG)

    # 회원 가입
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

    # 회원 탈퇴
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
