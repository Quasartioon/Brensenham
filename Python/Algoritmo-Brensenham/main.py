# 1 - calcular delta_x e delta_y
# 2 - x = xi e y = yi
# 3 - pdi = 2 * delta_y - delta_x
# 4 - plotar ponto x e y
# 5 - se pdi < 0, incrementa x + 1, calcula próximo pdi: pdi+1 = pdi + 2*delta_y
# 6 - se pdi >= 0, incrementa x+1 e y +1, calcula-se o próximo pdi: pdi + 1= pdi+2(delta_y - delta_x)
# 7 - repte-se passos 4 e 5 até o ponto final.

def brensenhamUsandoFor(xi, yi, xf, yf):
    delta_x = abs(xf - xi)
    delta_y = abs(yf - yi)

    step = delta_x if delta_x > delta_y else delta_y

    # em outras palavras:
    # if (delta_x > delxta_y):
    #   step = delta_x
    # else:
    #   step = delxta_y

    pixels = []
    x = xi
    y = yi
    pdi = 2 * delta_y - delta_x

    pixels.append(f"({x}, {y})")
    for i in range(step):
        if pdi < 0:
            x+=1
            pdi += 2*delta_y
            pixels.append(f"({x}, {y})")
        elif pdi >=0:
            x+=1
            y+=1
            pdi += 2*(delta_y - delta_x)
            pixels.append(f"({x}, {y})")

    print(",".join(pixels))

def brensenhamUsandoWhile(xi, yi, xf, yf):
    delta_x = abs(xf - xi)
    delta_y = abs(yf - yi)

    pixels = []
    x = xi
    y = yi
    pdi = 2 * delta_y - delta_x

    pixels.append(f"({x}, {y})")
    while True:
        if x == xf and y == yf:
            break
        if pdi < 0:
            x+=1
            pdi += 2*delta_y
            pixels.append(f"({x}, {y})")
        elif pdi >=0:
            x+=1
            y+=1
            pdi += 2*(delta_y - delta_x)
            pixels.append(f"({x}, {y})")

    print(",".join(pixels))

def main():
    print("Usando For e lógica de passo:")
    brensenhamUsandoFor(20, 10, 26, 15)

    print("Usando While SEM lógica de passos:")
    brensenhamUsandoWhile(20, 10, 26, 15)

if __name__ == "__main__":
    main()
