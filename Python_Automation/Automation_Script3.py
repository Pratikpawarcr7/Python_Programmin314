import sys
def main():

    if(len(sys.argv) == 2):

        if(sys.argv[1] == "--h" or sys.argv[1] == "--H"):
            print("This Automation Script Use to Travel the Directory")
            print("For Better Usage please check --u")

        elif(sys.argv[1] == "--u" or sys.argv[1] == "--U"):
            print("Please Excute the Script as")
            print("python FileName.py DirectoryName")
            print("DirectoryName should be absolute path")

        else:
            Directory_Name = sys.argv[1]
            print("Directory Name is :",Directory_Name)

    else:
        print("Invalid Number Of Arguments")
        print("Please use --h or --u more Information")

if __name__ == "__main__":
    main()  