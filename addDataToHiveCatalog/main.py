import functions as f
import cdc as c
import os
import time

def main():
    #Full Path and make sure forward slash is at the end!"
    path = '/mnt/c/Users/DrewNicolette/Desktop/testCatalog/testNew/'
    #Case sensitive column names!!"
    column_names = ['Id','First','Last','Add','City','State','Zip','Married']
    prev_file = 'cdfDataCatalog_prev.csv'
    curr_file = 'cdfDataCatalog_curr.csv'
    key='Id'

    f.checkPath(path)
    f.checkPrevFileExists(path,prev_file)
    f.checkArchiveDirsExist(path)
    if f.checkSum(path) == True:
        print("\nNo change in files")
        f.movePrevFile(path,prev_file)
        time.sleep(1)
        f.RenameCurrtoPrev(path,curr_file,prev_file)
        os._exit(0)
   
    c.addResultsFile(path,column_names,key)
    f.movePrevFile(path,prev_file)
    time.sleep(1)
    f.RenameCurrtoPrev(path,curr_file,prev_file)
    time.sleep(1)
    f.checkIfTSVExists(path,prev_file)
    time.sleep(1)
    f.convertToTabDelimitted(path,prev_file)

if __name__ == "__main__":
    main()
