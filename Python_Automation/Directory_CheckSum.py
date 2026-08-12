import os
import hashlib

def Find_Check_Sum(Vault):

     fobj = open(Vault,"rb")

     hobj = hashlib.md5()

     Buffered = fobj.read(1024)

     while(len(Buffered)>0):
          hobj.update(Buffered)
          Buffered = fobj.read(1024)  

     fobj.close()  

     return hobj.hexdigest()  

def Find_Duplicate(Directory):

    Ret = False

    Ret = os.path.exists(Directory)

    if (Ret == False):
        print("Path is invalid")
        return

    Ret = False

    Ret = os.path.isdir(Directory)
    
    if (Ret == False):
            print("It is Not A Directory")
            return

    Duplicate = {}

    for Folder_Name,Sub_FolderName,File_Name in os.walk(Directory):
         for fName in File_Name:
             fName = os.path.join(Folder_Name,fName)

             Check_Sum = Find_Check_Sum(fName)

          #   print(f"{fName}  : {Check_Sum}")

             if Check_Sum in Duplicate:

                  Duplicate[Check_Sum].append(fName)

             else:
                  
                  Duplicate[Check_Sum] = [fName]

    return Duplicate

def Delete_Duplicate(Directory_Name):

     MyDict = Find_Duplicate(Directory_Name)

     Result = list(filter(lambda x: len(x)>1,MyDict.values()))

     print(Result)

     Count = 0
     TotalDelete = 0

     for Value in Result:
         for subValue in Value:
              print(subValue)

              Count = Count + 1
              if(Count>1):
                   os.remove(subValue)
                   TotalDelete = TotalDelete + 1

         count = 0
     print("Total deleted files : ",TotalDelete)

def main():
    Delete_Duplicate("Marvellous")

if __name__ == "__main__":
    main()