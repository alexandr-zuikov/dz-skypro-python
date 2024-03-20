side = int(input("Введите сторону квадрата:"))

def square(side):
    area = side * side
    return area
    
area = square(side)
print("Площадь квадрата:", area)