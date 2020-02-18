OVERVIEW:
This project will do a Change data capture on two .csv files 
  - It will archive the previous version of the file and archive the changes to the file 
    - The previous version of the files will be stored in a prev_archive directory
    - The change between the current and previous files will be stored in a changed_archive directory as a json file
  - It also produces a .tsv(tab delimmited file)
 
Prereqs:
1. Python3
2. Packages: Hashlib, os, Path, glob, datetime, csv, time
Example: pip3 install Hashlib

** Make sure the packages are installed **

How to RUN THE FIRST TIME:
1. Clone the repo
2. Edit the main file:  
  2a. Change the path parameter to point to the directory where you want to keep a _curr file and a _prev file  
  2b. Change the column_names parameter to the columns of your csv file   
  2c. Change the key parameter to the key of your file
3. All you need to do now is create a .csv file in the directory you pointed to in step 2a. and name it the same as your curr_file parameter in the main.py file...  
Note: Using excel you can add/edit data to it or if you already have an excel file, save it as a .csv in that directory  
Note: Make sure file is closed and not open... You will get a permissions error if it is open  
4. Once those you added that file to that directory, run the main.py file (python3 main.py)  
  4a. It will prompt you to create a prev file and certain directories because it is your first time running and you won't have a previous file or achive directories..  
  4b. SO SAY YES TO ALL THE PROMPTS
5. The program will run...


How to RUN AFTER THE FIRST TIME:
1. Go into the directory where your curr and prev files are and your achive directories
Note: This is the same directory as the path parameter in the main.py file
2. Copy the prev csv file and rename to whatever your curr_file parameter is in the main.py file
3. Make the edits/deletes/additions you want to the curr file
Note: Leave the prev file ALONE!
4. Re-Run main.py (python3 main.py)
