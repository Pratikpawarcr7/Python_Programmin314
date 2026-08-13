#====================================
#
# Check Leap Year
#
#===================================

def main():

   Year = int(input("Enter the Year : "))

   if(Year % 4 == 0 and Year % 100 != 0 or Year % 400 ==0):
       print("Leap Year")
   else:
       print("Not a Leap Year")
       


if __name__ == "__main__":
    main()




