def CircleArea(fRadius):
    fArea = 0.0;
    fArea = 3.14 * fRadius * fRadius
    return fArea


def main():
   fValue1 = 0.0
   fResult = 0.0

   print("Enter the Radius of Circle")
   fValue1=float(input())

   fResult = CircleArea(fValue1)

   print("Area of circle is:",fResult)

if __name__ == "__main__":
    main()