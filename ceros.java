import java.util.Scanner;

class ceros{
    public static void main(String[] args) {
        double nota;
        int aprobados = 0, reprobados = 0;
        Scanner input = new Scanner(System.in);
        
        for (int i = 0; i < 6; i++){
            System.out.print(" No. " + (i+1) + " (0-10): ");
            nota = input.nextDouble();
            
            if (nota == 0){
                reprobados++;
            }else if ((nota >= 0) && (nota <= 10)){
                aprobados++;
            }
        }
        
        System.out.println("\nNumeros iguales a cero: " + reprobados);
        System.out.println("\nNumeros diferente de cero: " + aprobados);
    }
}