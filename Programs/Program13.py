def CheckEven(No):
    return No % 2 == 0

def main():

    Marks = [11,10,20,33,40,29,25]

    print("Data Before Filter : ",Marks)

    F_Data = list(filter(CheckEven,Marks))
    print("Data After Filter : ",F_Data)

if __name__ == "__main__":
    main()