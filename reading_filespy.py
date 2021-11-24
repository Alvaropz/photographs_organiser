import re
import os
from shutil import move

myTargetFolder = input('Type the path target with the YEAR of the pictures you want to copy/paste. Example -> C:\\Users\\User\\Desktop\\1569\nType your path: ')
mySourceFolder = input('Type the path source with the files of the pictures you want to copy/paste. Example -> C:\\Users\\Álvaro\\Desktop\\CopiedElements\nType your path: ')
monthList = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
pattern = "(\d{4})(\d{2})(\d{2})"

os.chdir(mySourceFolder)
myFiles = os.listdir("./")
for file in myFiles:
    formatedList = re.split(pattern, str(file))[1:4]
    year = formatedList[0]
    month = formatedList[1]
    day = formatedList[2]
    try:
        move("{}\{}".format(mySourceFolder, file), "{}\{}\{}".format(myTargetFolder, "{}. {}".format(month, monthList[int(month)-1]) , "{}-{}-{}".format(day, month, year)))
    except:
        continue

