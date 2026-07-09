CheckEven = lambda No : No % 2 == 0

def filterX(Task,Elements):

    Result = []
    for No in Elements:
        Ret = Task(No)

        if(Ret == True):
            Result.append(No)

    return Result

def main():

    Marks = [10,23,20,34,30,44,80]

    print("Marks Before Filter : ",Marks)

    F_Records = (filterX(CheckEven,Marks))
    print("Data After Filter : ", F_Records )

if __name__ == "__main__":
    main()

