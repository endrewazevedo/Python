
if __name__ == "__main__":
    n = int(input())
    lista = [0]*n

    for i in range(len(lista)):
        lista[n-1] = int(input())
        n -= 1

    print(lista)