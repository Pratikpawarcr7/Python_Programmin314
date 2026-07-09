CheckEven = lambda No : No % 2 == 0

Increment = lambda No : No + 1

def filterX(Task,Elements):

    Result = []
    for No in Elements:
        Ret = Task(No)

        if(Ret == True):
            Result.append(No)

    return Result

def mapX(Task,Elements):

    Result = []
    for No in Elements:
        Ret = Task(No)
        Result.append(No)

    return Result


def main():

    Marks = [10,23,20,34,30,44,80]

    print("Marks Before Filter : ",Marks)

    F_Records = (filterX(CheckEven,Marks))
    print("Data After Filter : ",  F_Records)

    M_Records = (mapX(Increment, F_Records))
    print("Data After Mapping : ", M_Records)

if __name__ == "__main__":
    main()
