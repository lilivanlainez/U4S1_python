year = int(input("Ingresa un año: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year, "es un año bisiesto.")
else:
    print(year, "no es un año bisiesto.")
