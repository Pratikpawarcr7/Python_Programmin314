from functools import reduce

CheckEven = lambda No : No % 2 == 0

Increment = lambda No : No + 1

Addition = lambda No1,No2 : No1 + No2

def main():

    Marks = [11,10,20,33,40,29,25]

    print("Data Before Filter : ",Marks)

    F_Data = list(filter(CheckEven,Marks))
    print("Data After Filter : ",F_Data)

    
    M_Data = list(map(Increment,F_Data))
    print("Data After Mapping : ",M_Data)

    R_Data = reduce(Addition,M_Data)
    print("Data After Reduce : ",R_Data)

if __name__ == "__main__":
    main()