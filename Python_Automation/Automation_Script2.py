import sys
def main():

    if(len(sys.argv) == 2):

        Directory_Name = sys.argv[1]
        print("Directory Name is :",Directory_Name)

    else:
        print("Invalid Number Of Arguments")

if __name__ == "__main__":
    main()