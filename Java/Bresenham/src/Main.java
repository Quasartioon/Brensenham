import java.util.ArrayList;
import java.util.List;
public class Main {
    public static void bresenhamUsandoFor(int xi, int yi, int xf, int yf){
        /*
        * 1 - calcular delta_x e delta_y
        * 2 - x = xi e y = yi
        * 3 - pdi = 2 * delta_y - delta_x
        * 4 - plotar ponto x e y
        * 5 - se pdi < 0, incrementa x + 1, calcula próximo pdi: pdi+1 = pdi + 2*delta_y
        * 6 - se pdi >= 0, incrementa x+1 e y +1, calcula-se o próximo pdi: pdi + 1= pdi+2(delta_y * delta_x)
        * 7 - repte-se passos 4 e 5 até o ponto final.
        * */

        //passo 1:
        int deltaX = Math.abs(xf - xi);
        int deltaY = Math.abs(yf - yi);

        int step = deltaX > deltaY ? deltaX : deltaY;

        // em outras palavras:
        /*int step;
        if (deltaX > deltaY){
            step = deltaX;
        }else{
            step = deltaY;
        }*/

        //passo 2:
        int x = xi, y = yi;
        //passo 3:
        int pdi = 2*deltaY-deltaX;
        //passo 7:
        List<String> pixels = new ArrayList<>();
        //passos 5 e 6:
        pixels.add("(" + x + "," + y + ")");
        for(int i = 0; i < step; i++){
            if (pdi < 0 ){
                x++;
                pdi += 2*deltaY;
                pixels.add("("+ x + "," + y +")");
            }else if (pdi >= 0){
                x++;
                y++;
                pdi += 2*(deltaY-deltaX);
                pixels.add("("+ x + "," + y +")");
            }
        }
        System.out.println(pixels);
    }

    /* Aqui o objetivo é tirar a dependência da variável step */
    public static void bresenhamUsandoWhile(int xi, int yi, int xf, int yf){
        // passo 1:
        int deltaX = Math.abs(xf - xi);
        int deltaY = Math.abs(yf - yi);

        //passo 2:
        int x = xi, y = yi;

        //passo 3:
        int pdi = 2*deltaY-deltaX;

        List<String> pixels = new ArrayList<>(); // exibir os pixels
        pixels.add("(" + x + "," + y + ")");
        while(true){
            if (x == xf && y == yf) break; // passo 7
            // passo 5:
            if (pdi < 0 ){
                x++;
                pdi += 2*deltaY;
                pixels.add("("+ x + "," + y +")");
            }else if (pdi >= 0){ // passo 6:
                x++;
                y++;
                pdi += 2*(deltaY-deltaX);
                pixels.add("("+ x + "," + y +")");
            }
        }

        System.out.println(pixels);
    }
    public static void main(String[] args) {
        System.out.println("Brensenham usando loop FOR COM a lógica de passos: ");
        bresenhamUsandoFor(20, 10, 26, 15);

        System.out.println("Brensenham usando loop WHILE SEM a lógica de passos:");
        bresenhamUsandoWhile(20, 10, 26, 15);
    }
}