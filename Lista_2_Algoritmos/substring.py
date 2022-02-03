from pickle import TRUE

def substring(sub, string):
    cont_sub = 0

    for i in range(len(string)):
        if sub[cont_sub] == string[i]:
            cont_sub += 1
            if cont_sub == len(sub):
                return 1
        else:
            cont_sub = 0
    return 0

if __name__ == "__main__":
    while TRUE:
        sub = str(input())
        if sub == "FIM": break
        else:
            string = str(input())
            if substring(sub, string) == 1:
                print("SIM\n")
            else: print("NAO\n")

