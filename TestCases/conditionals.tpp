program conditionals;

main() {
    vars
        float calificacion = 75.0;
        char letra;

        if (calificacion >= 90) {
            letra = 'A';
        } elif (calificacion >= 70) {
            letra = 'C';
        } else {
            letra = 'F';
        }

        switch(letra) {
            case 'A' {
                print("Muy buena calificacion \n");
            }
            case 'C' {
                print("Aprobado \n");
            }
            case 'F' {
                print("Reprobado \n");
            }
        }
}