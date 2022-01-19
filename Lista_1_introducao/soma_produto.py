from ast import If
from pickle import TRUE

if __name__ == "__main__":
    tupla = (2)
    while TRUE:
        tupla = eval(input())
        
        if tupla[0] == 0 and tupla[1] == 0: break
            
        else : print(tupla[0] + tupla[1],  tupla[0]*tupla[1]) 