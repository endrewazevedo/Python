from statistics import mean

if __name__ == "__main__":
    flag = 0
    while(flag == 0):
        tupla = eval(input())
        media = 0
        for i in range(len(tupla)):
            media += tupla[i]
        media = media/len(tupla)
        print("%.2f" % media)
        if(len(tupla) == 0):
            flag = 1