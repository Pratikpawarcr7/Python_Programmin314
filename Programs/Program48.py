# ==========================================================
# Program: Reverse a Number
# ==========================================================

Number = int(input("Enter a number: "))

Reverse = 0

while Number > 0:
    Digit = Number % 10
    Reverse = (Reverse * 10) + Digit
    Number = Number // 10

print("Reverse number is:", Reverse)