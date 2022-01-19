from pickle import FALSE, TRUE

def identidade(matriz):
    for i in range(len(matriz)):
        for j in range (len(matriz)):
            if lista[i][j] != 0 and i != j:
                return FALSE
            if i == j and lista[i][j] != 1:
                return FALSE
    return TRUE

if __name__ == "__main__":
    lista = []
    linhas = []
    lista = eval(input())
    
    if identidade(lista) == TRUE: print("sim")
    else: print("nao")
    