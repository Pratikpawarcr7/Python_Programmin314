#------------------------------------------------------------------------------------------------------------
# Question 2:
# Write a program that accepts one number as input and prints the sum of the first N natural numbers.
# Example:
# Input: 5
#
# Output:
#     15
#-------------------------------------------------------------------------------------------------------------

def Nutural_Num(No):

    Sum = 0 

    for iCnt in range(0,No+1):
        Sum = Sum + iCnt

    return Sum

def main():

    Ret = 0
    Value = 0
    print("Enter the Number : ")
    Value = int(input())

    Ret = Nutural_Num(Value)

    print("sum of the first N natural numbers : ",Ret)


if __name__ == "__main__":
    main()

