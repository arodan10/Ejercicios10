import java.util.Scanner;

class ejercicio{
    public static void main(String[] args) {
        double nota;
        int aprobados = 0, aprobadosConExcelencia = 0, reprobados = 0;
        Scanner input = new Scanner(System.in);
        
        for (int i = 0; i < 6; i++){
            System.out.print("Nota del alumno No. " + (i+1) + " (1-5): ");
            nota = input.nextDouble();
            
            if ((nota >= 1) && (nota < 3)){ //Entre 1.0 y 2.9 se pierde
                reprobados++;
            }else if ((nota >= 3) && (nota < 4.7)){ //A partir de 3.0 se gana
                aprobados++;
            }else if ((nota >= 4.7) && (nota <= 5)){ //A partir de 4.7 es excelente
                aprobadosConExcelencia++;
            }
        }
        
        System.out.println("\nAlumnos reprobados: " + reprobados);
        System.out.println("Alumnos aprobados: " + aprobados);
        System.out.println("Alumnos aprobados con excelencia: " + aprobadosConExcelencia);
    }
}