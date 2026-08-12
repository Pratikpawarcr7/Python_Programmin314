import hashlib
def Calculate_CheckSum(FileName):

    fobj = open(FileName,"rb")

    hobj = hashlib.md5()

    Data = fobj.read(1024)

    while(len(Data)>0):
        hobj.update(Data)
        Data = fobj.read(1024)

    fobj.close()

    return hobj.hexdigest()

def main():

    Ret = Calculate_CheckSum("Demo.txt")

    print("CheckSum of File is : :",Ret)

if __name__ == "__main__":
    main()