# the writer function returns file object and provides delimiter for csv file
# a delimiter is  ,  or |   to separate the values of csv file
# you can open csv files similarly as ordinary files
# along with the writer object you can write rows with the writerow method

import csv

with open("string.csv", "w") as f:
    write = csv.writer(f, delimiter=",")
    write.writerow(["Top Gun", "Risky Business", "Minority Report"])
    write.writerow(["Titanic", "The Revenant", "Inception"])
    write.writerow(["Titanic", "The Revenant", "Inception"])

with open("string.csv", "r") as f:
    read = csv.reader(f, delimiter=",")
    for row in read:
        print(",".join(row))

