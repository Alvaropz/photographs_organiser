import os
import calendar

yearStr = input("Give a year: ")
# Warning - os.getenv('username') cannot handle usernames with special characters such as accents.
dirName = '{}/Users/{}/Desktop/{}'.format(os.getenv("SystemDrive"), os.getenv('username'), yearStr) 
try:
    # Creates target Directory
    os.mkdir(dirName)
    print(yearStr, "folder created")
    os.chdir(dirName)

    monthList = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre",
    "Octubre", "Noviembre", "Diciembre"]
    
    for month in range(1, 13):
        if month < 10:
            formatedMonth = "0" + str(month) + ". " + monthList[month-1]
        else:
            formatedMonth = str(month) + ". " + monthList[month-1]
        os.mkdir('{}'.format(formatedMonth))
        os.chdir('./{}'.format(formatedMonth))
        
        dayTuple = calendar.monthrange(int(yearStr), month)

        if month < 10:
            monthStr = "0" + str(month)
        else:
            monthStr = str(month)

        for day in range(1, dayTuple[1]+1):
            if day < 10:
                os.mkdir('0{}-{}-{}'.format(day, monthStr, yearStr))
            else:
                os.mkdir('{}-{}-{}'.format(day, monthStr, yearStr))
        
        os.chdir('../')
    
except FileExistsError:
    print("Directory " , yearStr ,  " already exists")