from API.create import Create
from API.conversion import Conversion
from API.timer import Timer


timer = Timer()
cre = Create()
con = Conversion()
timer.CountDown()

if __name__ == '__main__':
    start = timer.__Start__()
    for i in range(10):
        Decimal_Data = cre.Create_Decimal()
        print(Decimal_Data)
        con.test(con.Decimal_To_Binary(Decimal_Data))
    end = timer.__End__()
    count = timer.Count(__Start__=start, __End__=end)
    print(f"종료\n모든 10진수를 변환 하였 습니다.\n총 걸린 시간 : {count}")
