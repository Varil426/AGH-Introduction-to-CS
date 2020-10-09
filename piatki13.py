import datetime
for i in range (2017,2019):
    for j in range (1,13):
        if datetime.datetime(i,j,13).weekday() == 4:
            print("13 .",j,".",i)