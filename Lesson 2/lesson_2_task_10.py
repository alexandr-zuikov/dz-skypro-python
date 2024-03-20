X = int(input("Сумма вклада:"))
Y = int(input("Срок вклада:"))

def bank(X, Y):
    for year in range(Y):
        X += X * 0.10
    return X

print (bank(X, Y))