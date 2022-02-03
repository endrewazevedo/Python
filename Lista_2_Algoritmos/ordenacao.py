from pickle import FALSE, TRUE


def ordena(lista):
    for j in range(len(lista)):
        flag = FALSE
        for i in range(len(lista) - 1):
            if lista[i] > lista[i+1]:
                flag = TRUE
                aux = lista[i]
                lista[i] = lista[i+1]
                lista[i+1] = aux
        if flag == FALSE:
            break

if __name__ == "__main__":
    while TRUE:
        lista = eval(input())
        if lista == []:
            break
        ordena(lista)
        print(lista)
        