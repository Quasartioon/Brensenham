# 1 - calcular delta_x e delta_y
# 2 - x = xi e y = yi
# 3 - pdi = 2 * delta_y - delta_x
# 4 - plotar ponto x e y
# 5 - se pdi < 0, incrementa x + 1, calcula próximo pdi: pdi+1 = pdi + 2*delta_y
# 6 - se pdi >= 0, incrementa x+1 e y +1, calcula-se o próximo pdi: pdi + 1= pdi+2(delta_y - delta_x)
# 7 - repte-se passos 4 e 5 até o ponto final.


def brensenhamUsandoFor(xi, yi, xf, yf):
    # passo 1
    delta_x = abs(xf - xi)
    delta_y = abs(yf - yi)

    step = delta_x if delta_x > delta_y else delta_y  # passo 7

    # em outras palavras:
    # if (delta_x > delxta_y):
    #   step = delta_x
    # else:
    #   step = delxta_y

    # passo 2
    x = xi
    y = yi

    # passo 3
    pdi = 2 * delta_y - delta_x

    # passo 4
    pixels = []
    pixels.append(f"({x}, {y})")

    for i in range(step):  # passo 7
        if pdi < 0:  # passo 5
            x += 1
            pdi += 2 * delta_y
            pixels.append(f"({x}, {y})")  # passo 4
        elif pdi >= 0:  # passo 6
            x += 1
            y += 1
            pdi += 2 * (delta_y - delta_x)
            pixels.append(f"({x}, {y})")  # passo 4

    print(",".join(pixels))


def brensenhamUsandoWhile(xi, yi, xf, yf):
    # passo 1
    delta_x = abs(xf - xi)
    delta_y = abs(yf - yi)

    # passo 2
    x = xi
    y = yi

    # passo 3
    pdi = 2 * delta_y - delta_x

    # passo 4
    pixels = []
    pixels.append(f"({x}, {y})")

    while True:
        if x == xf and y == yf:  # passo 7
            break
        if pdi < 0:  # passo 5
            x += 1
            pdi += 2 * delta_y
            pixels.append(f"({x}, {y})")
        elif pdi >= 0:  # passo 6
            x += 1
            y += 1
            pdi += 2 * (delta_y - delta_x)
            pixels.append(f"({x}, {y})")  # passo 4

    print(",".join(pixels))


def main():
    print("Usando For e lógica de passo:")
    brensenhamUsandoFor(20, 10, 26, 15)

    print("Usando While SEM lógica de passos:")
    brensenhamUsandoWhile(20, 10, 26, 15)


if __name__ == "__main__":
    main()
