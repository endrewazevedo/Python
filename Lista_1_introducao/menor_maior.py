if __name__ == "__main__":
    for i in range(10):
        num = int(input())
        if i == 0:
            maior = num
            menor = num
        if num < menor: menor = num
        if num > maior: maior = num
    print(menor, maior)