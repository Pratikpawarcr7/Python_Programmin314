def Display(iSize):
    
    Marks = []
    iSum = 0
    print("Enter the Elements : ")
    iNo1 = 0

    for iCnt in range(iSize):
        iNo1 = int(input())
        Marks.append(iNo1)

    print(Marks)  

    for iCnt in range(len(Marks)):
        iSum = iSum + Marks[iCnt]

    return iSum

def main():
    
    print("How Many Elments you Want in Your List : ")
    iValue = int(input())

    iRet =  Display(iValue)

    print("Summation : ",iRet)

if __name__ == "__main__":
    main()















