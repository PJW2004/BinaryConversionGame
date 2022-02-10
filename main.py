from API.create import Create
from API.conversion import Conversion
from API.timer import Timer
from DB.Datainput import MAIN_Start
from DB.UserConnecting import MAIN_CONNECT
from DB.RANK import rankSCORE


# Instance
timer = Timer()
cre = Create()
con = Conversion()
db = MAIN_Start()
user = MAIN_CONNECT()
rank = rankSCORE()


# 실제 동작 페이지
def RUN(UserName=""):
    try:
        # rank.user_SCORE()
        Answer = int(input("단계를 1~5중 선택 하시오. [종료를 원할시 아무 키나 누르면 됩니다.] \n>>"))
        timer.CountDown()
        start = timer.__Start__()
        for i in range(10):
            Decimal_Data = cre.Create_Decimal(cre.Choose_Step(User_Answer=Answer), User_Answer=Answer)
            print(Decimal_Data)
            con.test(con.Decimal_To_Binary(Decimal_Data, User_Answer=Answer))
        end = timer.__End__()
        count = timer.Count(__Start__=start, __End__=end)
        print(f"종료\n모든 10진수를 변환 하였 습니다.\n총 걸린 시간 : {count}")
        db.InputLOG(DBNAME="LOG", HEAD=f"[{Answer}]{UserName}", LOG=f"[time={count}]")

        RUN(UserName=UserName)

    except ValueError:
        print("Program 을 종료 합니다.")


# user connect 과정
def CONNECT():
    UserName = input("[IF YOU WANT DELETE YOUR USERID PLEASE WRITE KEY 'A']\nUserName : ")

    # USERID 삭제
    if UserName == "A":
        db.withdrawal()

    # USERID 입력창
    else:
        Password = input("Password : ")

        user.CONNECT(User=UserName, pwd=Password)

        if user.State == "MAIN CONNECTING":
            RUN(UserName=UserName)

        # 회원 가입
        elif user.State == "Sign Up":
            UserAnswer = db.SignUPAnswer()
            if UserAnswer == "Y":
                db.SignUp()
                CONNECT()
            else:
                CONNECT()

        else:
            print("SORRY INFORMATION DOSE NOT EXIST\n")
            CONNECT()


# 동작 하는 곳
if __name__ == '__main__':
    CONNECT()
