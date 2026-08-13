#====================================
#
# Fubonacci Series
#
#===================================

def main():

   Value = int(input("Number of Term : "))
   a,b = 0,1

   for _ in range(Value):
       print(a,end=" ")
       a,b = b, a + b


if __name__ == "__main__":
    main()




