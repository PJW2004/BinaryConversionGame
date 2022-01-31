class MAIN_Start:
    def __init__(self):
        with open("./DB/USER_DB", "w") as Userdata:
            Userdata.write(f"admin:admin123,\n")
            Userdata.close()
