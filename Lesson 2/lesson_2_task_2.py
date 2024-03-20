year = int(input("Введите год:"))

if year % 4 == 0:
    print("Год " + str(int(year)) + ":", "True")
else:
    print("Год " + str(int(year)) + ":", ": False")