# Implementação do algoritmo de Bresenham em Java e Python


## O que é algoritmo de Brensenham?
O algoritmo de Bresenham é um método para rasterizar linhas em uma grade de pixels usando apenas operações inteiras.  

Dado dois pontos (xi, yi) e (xf, yf), ele percorre o eixo principal (geralmente o eixo x) e decide, a cada passo, qual pixel vizinho melhor aproxima a reta ideal. Essa decisão é feita com base em um erro acumulado, que representa a diferença entre a posição real da linha (contínua) e a posição discreta do pixel escolhido.  

A lógica central é:  
* Incrementar um eixo de forma constante (ex: x)  
* Atualizar um termo de erro  
* Usar esse erro para decidir quando incrementar o outro eixo (ex: y)  

Isso evita o uso de números de ponto flutuante, tornando o algoritmo eficiente e determinístico para desenho de linhas em sistemas raster.  

## Como fazer isso?
1. calcular delta_x e delta_y;  
2. x = xi e y = yi;  
3.  pdi = 2 * delta_y - delta_x;  
4. plotar ponto x e y;  
5. se pdi < 0, incrementa x + 1, calcula próximo pdi: pdi+1 = pdi + 2*delta_y;  
6. se pdi >= 0, incrementa x+1 e y +1, calcula-se o próximo pdi: pdi + 1= pdi+2(delta_y - delta_x);  
7. repte-se passos 4, 5 e 6 até o ponto final.  

## O que o repositório fornece?
Uma implementação do núcleo matemático do algoritmo, explorando duas abordagens:
* Com eixo dominante:  
    Identifica qual delta é maior para definir o eixo principal e o limite do loop (for).  
* Sem eixo dominante explícito:  
    Utiliza um while contínuo e encerra quando (x, y) atinge (x_f, y_f). 

## Por que em Java e em Python?
A proposta é comparar como cada linguagem se comporta na implementação do mesmo algoritmo, destacando diferenças de sintaxe, controle de fluxo e expressividade.

## Extra
Inclui também uma versão em C++, com foco em estudos de baixo nível e proximidade com hardware.  

## O que melhorar
* Substituir multiplicações por 2 por operações bitwise (<< 1) como micro-otimização
* Generalizar para todos os octantes (caso ainda não esteja coberto)
* Separar lógica de cálculo da lógica de renderização
* Adicionar testes automatizados
