import sys
import os
def Directory_Scanner(Directory_Path):

    for FolderName,SubFolder_Name,File_Name in os.walk(Directory_Path):
        for fName in File_Name:
            print(fName)
        

def main():

    print("------------------------------------------------------")
    print(" Marvellous Automation Script ")
    print("------------------------------------------------------")

    if(len(sys.argv) == 2):

        if(sys.argv[1] == "--h" or sys.argv[1] == "--H"):
            print("This Automation Script Use to Travel the Directory")
            print("For Better Usage please check --u")

        elif(sys.argv[1] == "--u" or sys.argv[1] == "--U"):
            print("Please Excute the Script as")
            print("python FileName.py DirectoryName")
            print("DirectoryName should be absolute path")

        else:
            Directory_Scanner(sys.argv[1])
            

    else:
        print("Invalid Number Of Arguments")
        print("Please use --h or --u more Information")


    print("------------------------------------------------------")
    print(" Thank you For Using Marvellous Automation Script ")
    print("------------------------------------------------------")

if __name__ == "__main__":
    main()  