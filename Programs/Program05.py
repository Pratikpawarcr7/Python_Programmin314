def Display(iNo):

    iCnt = 0
    while(iCnt<iNo):
        print("Jay Ganesh...")
        iCnt = iCnt + 1

def main():
    print("Enter the Frequency")
    iValue1 = int(input())

    Display(iValue1)
    
if __name__ == "__main__":
    main()