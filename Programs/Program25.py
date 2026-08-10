def main():

    fobj = open("Marvellous_Infosystem.txt","r")

    print("Offset is : ",fobj.tell())

    Data = fobj.read(10)

    print(Data)

    print("Offset is : ",fobj.tell())
    
    Data = fobj.read(10)
    
    print(Data)

if __name__ == "__main__":
    main()