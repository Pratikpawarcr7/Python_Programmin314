
def main():

    try:
        fobj = open("Marvellous_Infosystem.txt","w")

        print("File is created Succesfully")
       
        fobj.write("Marvellous Infosystem Pune\n")
       
        fobj.write("Kothroad Pune")
       

    except Exception as eobj:
        print("File is not Present in Directory")


if __name__ == "__main__":
    main()