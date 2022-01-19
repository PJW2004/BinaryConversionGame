from time import time
from time import sleep


class Timer:

    def __Start__(self):
        S_time = time()
        return S_time

    def __End__(self):
        E_time = time()
        return E_time

    def Count(self, __Start__, __End__):
        count = __End__ - __Start__
        return count

    def CountDown(self):
        print("카운트 다운을 시작 합니다.\n")
        for i in range(1, 6):
            print(i)
            sleep(1)
        print('시작\n다음 주어 지는 10개의 10진수 들을 2진수로 변환 하시오\n')
