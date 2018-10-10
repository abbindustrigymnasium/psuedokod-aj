num1 = input("Hur många månader får du studiebidrag under dina tre år i gymnasiet?")
num2 = input("Hur mycket får du i studiebidrag per månad?")
num3 = input("Vilken månad är du född? skriv som en siffra.")
product = int(num1) * int(num2)
if int(num3)== 7 or int(num3) == 8 or int(num3) == 9:
    product = int(product) - 1875
    print(product, "kr")
else:
    print(product, "kr")
