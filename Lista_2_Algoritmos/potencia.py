def pot(x,y):
    if y == 0:
        return 1
    elif(y > 0):
        return x * pot(x,y-1)
    else:
        return 1/x * pot(x,y+1)

if __name__ == "__main__":
    numerador = eval(input())
    expoente = eval(input())
    for i in range(len(numerador)):
        for j in range(len(expoente)):
             print("{x:.4f}".format (x = pot(numerador[i], expoente[j])))