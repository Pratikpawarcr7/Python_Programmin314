import schedule
import time
import datetime
import os
import sys

border = "="*40

def Directory_Name(Directory_Entry):

    timeStamp = time.ctime()

    logFile = "Marvellous%s.Log"%(timeStamp)
    logFile = logFile.replace(" ","_")
    logFile = logFile.replace(":","_")
    fobj = open(logFile,"w")

    fobj.write(border+"\n")
    fobj.write("Marvellous Automation Script")
    fobj.write("\n"+border+"\n")
    fobj.write("Files in Folders Are:-")
    fobj.write("\n"+border+"\n")

    Total = 0
    Delete = 0

    for Folder_Name , SubFolder_Name,File_Name in os.walk(Directory_Entry):
        for fName in File_Name:
            fobj.write(fName+"\n")
            fName = os.path.join(Folder_Name,fName)
            Total = Total + 1
            if(os.path.getsize(fName) == 0):
                Delete = Delete + 1
                os.remove(fName)
            

    print(border)
    print("Log File Gets Created by : ",timeStamp)
    print(border)
    fobj.write(border+"\n")
    fobj.write(f"Log File Gets Created by : {timeStamp}")
   
    fobj.write("\n"+border+"\n")
    fobj.write(f"Total File Scanned : {Total}")
    fobj.write("\n"+border+"\n")

    fobj.write(f"Total Deleted Files : {Delete}")
    fobj.write("\n"+border+"\n")

    fobj.close()


def main():
    print(border)
    print("Wlecome To Marvellous Automation Script ")
    print(border)

    if(len(sys.argv)== 2):
        if(sys.argv[1] == "--h" or sys.argv[1] == "--H"):
            print("Help==>")
            print(border)
            print("1). This Automation Script Use to Delete files which Contain 0 bytes and also Delete the Duplicate Files")
            print(border)
            print("2). If You Want To Run This Application Please Please Enter --U")
            print(border)

        elif(sys.argv[1] == "--U" or sys.argv[1] == "--u"):
            print("Usages==>")
            print(border)
            print("1).Run The Code in Folloing Command ==>")
            print(border)
            print("python FileName.py DirectoryName")
            print(border)

        else:

           # Directory_Name(sys.argv[1])
           schedule.every(1).minutes.do(Directory_Name,sys.argv[1])

           while True:
               schedule.run_pending()
               time.sleep(1)
           

    else:
        print(border)
        print("Thank you For Using Marvellous Automation Script")
        print(border)


if __name__ == "__main__":
    main()