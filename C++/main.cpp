#include <iostream>
#include <vector>
#include <ostream>
#include <string>
/*
* 1 - calcular delta_x e delta_y
* 2 - x = xi e y = yi
* 3 - pdi = 2 * delta_y - delta_x
* 4 - plotar ponto x e y
* 5 - se pdi < 0, incrementa x + 1, calcula próximo pdi: pdi+1 = pdi + 2*delta_y
* 6 - se pdi >= 0, incrementa x+1 e y +1, calcula-se o próximo pdi: pdi + 1= pdi+2(delta_y - delta_x)
* 7 - repte-se passos 4 e 5 até o ponto final.
*/

void brensenhamUsandoFor(int xi, int yi, int xf, int yf){
    int deltaX = abs(xf - xi);
    int deltaY = abs(yf - yi);

    int step = deltaX > deltaY ? deltaX : deltaY;

    int x = xi;
    int y = yi;
    int pdi = 2 * deltaY-deltaX;
    std::vector<std::string> pixels;
    pixels.push_back("(" + std::to_string(x) + "," + std::to_string(y) + ")");
    for(int i = 0; i < step; i++){
        if(pdi < 0){
            x++;
            pdi += 2*deltaY;
            pixels.push_back("(" + std::to_string(x) + "," + std::to_string(y) + ")");
        }else if(pdi >=0){
            x++;
            y++;
            pdi += 2*(deltaY-deltaX);
            pixels.push_back("(" + std::to_string(x) + "," + std::to_string(y) + ")");
        }
    }
    for(std::string i : pixels){
        std::cout << i << ",";
    }
    std::cout << std::endl;
}

void brensenhamUsandoWhile(int xi, int yi, int xf, int yf){
    int deltaX = abs(xf - xi);
    int deltaY = abs(yf - yi);

    int x = xi;
    int y = yi;
    int pdi = 2 * deltaY-deltaX;
    std::vector<std::string> pixels;

    pixels.push_back("(" + std::to_string(x) + "," + std::to_string(y) + ")");
    while(true){
        if(x == xf && y == yf) break;
        if(pdi < 0){
            x++;
            pdi += 2*deltaY;
            pixels.push_back("(" + std::to_string(x) + "," + std::to_string(y) + ")");
        }else if(pdi >=0){
            x++;
            y++;
            pdi += 2*(deltaY-deltaX);
            pixels.push_back("(" + std::to_string(x) + "," + std::to_string(y) + ")");
        }
    }

    for(std::string i : pixels){
        std::cout << i << ",";
    }
    std::cout << std::endl;
}

int main(){
    std::cout << "Brensenham usando loop For, COM lógica de passo: " << std::endl;
    brensenhamUsandoFor(20, 10, 26, 15);

    std::cout << "Brensenham usando loop While, SEM lógica de passo: " << std::endl;
    brensenhamUsandoWhile(20, 10, 26, 15);
    return 0;
}
