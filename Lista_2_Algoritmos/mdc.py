def mdc(num1, num2):
    num1 = abs(num1)
    num2 = abs(num2)

    if num1 == 0 or num2 == 0:
        if(num1 != 0): return num1
        else: return num2
        

    if num1 == num2: return num1

    elif num1 > num2: maior = num1

    else:
        maior = num2
        num2 = num1

    while maior != num2:
        maior -= num2
        if num2 > maior:
            aux = maior
            maior = num2
            num2 = aux
         
    return maior

if __name__ == "__main__":
    num1 = int(input())
    num2 = int(input())
    print(mdc(num1,num2))