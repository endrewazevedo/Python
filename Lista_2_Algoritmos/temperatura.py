def converte(temperatura):
    return temperatura * 1.8 + 32

if __name__ == "__main__":
    temperatura = float(input())
    print("{x:.1f}".format (x = converte(temperatura)))