#====================================
#
# List Comparihesion  
#
#===================================

Chk_Square = lambda No : No**2

def main():

    fData = []

    num = [4,6,2,5,6]

    print("Data Before Filter : ", num)

    fData = list(filter(Chk_Square,num))

    print("Data After Filter : ", fData)
       
if __name__ == "__main__":
    main()




