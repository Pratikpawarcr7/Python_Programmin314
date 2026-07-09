def Addition(iNo1,iNo2):

    iResult = iNo1 +iNo2
    return iResult

def main():

    iValue1 = int(input("Enter the First Number  :"))
    iValue2 = int(input("Enter the Second Number :"))

    iRet = Addition(iValue1,iValue2)
    print("Addition :",iRet)

if __name__ == "__main__":
    main()