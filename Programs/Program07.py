def Addition(iNo1,iNo2):

    iResult = iNo1 +iNo2
    return iResult

def main():
    print("Enter the First Number")
    iValue1 = float(input())

    print("Enter the Second Number")
    iValue2 = float(input())

    iRet = Addition(iValue1,iValue2)
    print("Addition :",iRet)

if __name__ == "__main__":
    main()