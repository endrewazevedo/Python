def imposto(salario):
    return (salario/100)*11

def inss(salario):
    return (salario/100)*8

def calc_salario(valor_horas, horas):
    return valor_horas * horas


if __name__ == "__main__":
    valor = int(input())
    horas = int(input())
    salario = calc_salario(horas, valor)
    print(imposto(salario)) # Quanto pagou de Imposto de Renda
    print(inss(salario)) # Quanto Fernando pagou ao INSS
    print(salario - inss(salario) - imposto(salario)) # Salario líquido
    print(inss(salario) + imposto(salario)) # Total de desconto