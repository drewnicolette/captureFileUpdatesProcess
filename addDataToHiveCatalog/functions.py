import hashlib
import os
from pathlib import Path
import glob
from datetime import datetime
import csv

def checkPath(path):
    if not os.path.exists(path):
        print("Path does not exist")
        os._exit(1)

def checkPrevFileExists(path,prevFile):
    filesInDir = [file for file in os.listdir(path)]   
    joinedList = "".join(filesInDir)
 
    if 'prev.' not in joinedList:
        print("\n'prev' file does not exist there")
        createFile = input("\nDo you want to create it? (yes/no): ")
        if createFile=='yes':
            createPrevFile = "".join([path,prevFile])
            Path(createPrevFile).touch()
            print("\nPrev File Created")

def checkArchiveDirsExist(path):
    prevDir = "".join([path,'prev_archive'])
    resultDir = "".join([path,'changed_archive'])
    filesInDir = [file for file in os.listdir(path)]
    joinedList = "".join(filesInDir)

    if ('prev_' not in joinedList) and ('changed_' not in joinedList):
        print("\nBoth the 'prev' and 'changed' folders do not exist")
        createThem = input("\nDo you want to create them both? (yes/no): ")
        if createThem == 'yes':
            os.mkdir(prevDir)
            os.mkdir(resultDir)
        else:
            print("\nThese are needed for process to work... please create")
            os._exit(1)
    elif ('prev_' not in joinedList) and ('changed_' in joinedList):
        print("\nThe 'prev' archive folder does not exist")
        createPrev = input("\nDo you want to create the 'prev' directory? (yes/no): ")
        if createPrev == 'yes':
            os.mkdir(prevDir)
        else:
            print("\nThis is needed for process to work... please create")
            os._exit(1)
    elif ('prev_' in joinedList) and ('changed_' not in joinedList):
        print("\nThe 'result' folder does not exist")
        createCurr = input("\nDo you want to create the 'changed' directory? (yes/no): ")
        if createCurr == 'yes':
            os.mkdir(resultDir)
        else:
            print("\nThis is needed for process to work... please create") 
            os._exit(1)

def checkSum(path):
    csv_files = glob.glob("".join([path,'*.csv']))
    if len(csv_files) < 2:
        print("\nPlease check both the _curr and _prev file exist!")
        os._exit(0)

    digests = []
    for filename in csv_files:
        hasher = hashlib.md5()
        with open(filename, 'rb') as f:
            buf = f.read()
            hasher.update(buf)
            get_hash = hasher.hexdigest()
            digests.append(get_hash)

    if digests[0] == digests[1]:
        return True
    else:
        return False 

def movePrevFile(path,prev_file):
    full_path = "".join([path,prev_file])
    fileSplit = os.path.splitext(prev_file)[0]
    dateTime = datetime.now()
    dateTimeStr = dateTime.strftime("%m_%d_%Y_%H:%M:%S")
    filename = "".join([fileSplit,dateTimeStr,".csv"])
    filenameAndPath = "".join([path,'prev_archive/',filename])
    os.rename(full_path,filenameAndPath)

def RenameCurrtoPrev(path,curr_file,prev_file):
    fullCurrPath = "".join([path,curr_file])
    fullPrevPath = "".join([path,prev_file])
    os.rename(fullCurrPath,fullPrevPath)

def convertToTabDelimitted(path,file):
    inFile = "".join([path,file])
    fileSplit = "".join([os.path.splitext(file)[0],'tar'])
    outFile = "".join([path,fileSplit,".tsv"])
    headerRow = input("\nDoes your file have a header row? (yes/no): ")
    
    if headerRow == 'yes':
        with open(inFile,'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            next(csv_reader)
            for line in csv_reader:
                with open(outFile,'a') as new_txt:
                    txt_writer = csv.writer(new_txt, delimiter = '\t')
                    txt_writer.writerow(line)
    elif headerRow == 'no':
        with open(inFile,'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            
            for line in csv_reader:
                with open(outFile,'a') as new_txt:
                    txt_writer = csv.writer(new_txt, delimiter = '\t')
                    txt_writer.writerow(line)

def checkIfTSVExists(path,file):
    filesInDir = [file for file in os.listdir(path)]
    joinedList = "".join(filesInDir)
    tsv_archive = "".join([path,"tsv_archive"])
    
    #Change the incoming prev file to tsv extension
    inFile = "".join([path,file])
    fileSplit = "".join([os.path.splitext(file)[0],'tar'])
    outFile = "".join([path,fileSplit,".tsv"])

    dateTime = datetime.now()
    dateTimeStr = dateTime.strftime("%m_%d_%Y_%H:%M:%S")
    filename = "".join([fileSplit,dateTimeStr,".tsv"])
    filenameAndPath = "".join([path,'tsv_archive/',filename])

    if 'tsv_' not in joinedList:
        os.mkdir(tsv_archive)

    if '.tsv' in joinedList:
        os.rename(outFile,filenameAndPath)
        
