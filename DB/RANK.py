class rankSCORE:
    def __init__(self):
        user_DB = {}

    def user_SCORE(self):
        with open("./DB/RANK") as user_SCORE:
            with open("./DB/LOG") as LOG:
                for data in LOG:
                    name = data.split(':')[0][3:]
                    time = data.split(':')[1][6:]
                    print(name, time)

                LOG.close()

            user_SCORE.close()
