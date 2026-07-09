def CheckEven(No):
    return No % 2 == 0

def Increment(No):
    return No + 1

def main():

    Marks = [11,10,20,33,40,29,25]

    print("Data Before Filter : ",Marks)

    F_Data = list(filter(CheckEven,Marks))
    print("Data After Filter : ",F_Data)

    
    M_Data = list(map(Increment,F_Data))
    print("Data After Mapping : ",M_Data)

if __name__ == "__main__":
    main()