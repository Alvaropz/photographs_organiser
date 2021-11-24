# Photographs Organiser

## Table of Contents:

* [General Info](#general-info)
* [Technologies](#techonologies)
* [Setup](#setup)

## General Info:

This was my very first original problem to solve a problem organisating pictures as I have a my own personal way to organise them in folders. I used to do it manually, then, I thought there would be a way to automate the process by writing a simple program so I did it.

This project includes two programs:

* "creating_year_folder.py" asks you to type a "year" (f.e.: 2021) when you run the program. Then, it automatically creates folders and subfolders with all months (f.e: "01. January" format) and days (f.e: "02-04-2021" format) for each month. As this project was designed to work in Windows, the year folder is created in the "Desktop" folder, as it's usually easy to find any file there.

* "reading_filespy.py" requests two paths, the first path is related to the target folder where you want to organise your pictures. The second path is the source folder where you want to take your pictures of. Reached this point, it's important to say that the program is designed to handle the format "20200101_221106" which stands for "yyyymmdd_hhmmss". Said this, the program reads every file name, then if it finds a right place, it cuts the picture, then it pastes it in the right folder.

## Technologies:

Project is created with:
* Visual Studio Code
* Git
* GitHub
* Python for Visual Studio Code

## Setup:

* Git: [Git - Installation](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* Visual Studio Code: [Visual Studio Code](https://code.visualstudio.com)
