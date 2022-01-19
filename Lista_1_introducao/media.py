from pickle import TRUE
from statistics import mean

if __name__ == "__main__":
    while TRUE:
        tupla = eval(input())
        if tupla == tuple(): break
        else:      
            media = sum(list(tupla))/len(list(tupla))
            print("{x:.2f}".format (x = media))
