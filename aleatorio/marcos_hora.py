import datetime

now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%s")

with open("date_time", "w") as arq_hora:
    arq_hora.write(now)

