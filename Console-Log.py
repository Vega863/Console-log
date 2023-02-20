import os
import datetime


def log():
    date = datetime.datetime.now()
    if os.path.exists("log.txt") == False:
        with open("log.txt", "w") as file:
            file.write(f"[Date - {date} ] Connexion User Sessions : 0 ")
    with open("log.txt", "r") as file:
        contents = file.read()
        try:
            num = contents
            num = num.split(" ")[-1]
            num = int(num)
        except ValueError:
            num = 0
    with open("log.txt", "a") as file:
        num += 1
        num = str(num)
        file.write(
            str(f'\n[Date  -{date} ] Connexion User Sessions : {num}'))
        


if __name__ == "__main__":
    log()
