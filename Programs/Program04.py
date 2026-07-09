def CalculatePercentage(iObtained, iTotal):
    fPercentage = float(iObtained) / float(iTotal) * 100
    return fPercentage

def main():
    print("Please enter obtain mark in your exam")
    iValue1=int(input())

    print("Enter the Obtain Marks")
    iValue2=int(input())

    fResult = CalculatePercentage(iValue1, iValue2)

    print("Your percentage is:", fResult)

if __name__ == "__main__":
    main()