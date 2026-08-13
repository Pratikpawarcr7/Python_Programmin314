#====================================
#
# List Comparihesion  
#
#===================================

Chk_Square = lambda No : No**2

def main():

    fData = []

    num = [1,2,3,4,5,6,7,8,9,10]

    print("Data Before Filter : ", num)

    fData = list(map(Chk_Square,num))

    print("Data After Filter : ", fData)
       
if __name__ == "__main__":
    main()




