program functions;

func int multiply(int a, int b) {
    return(a*b);
}

main() {
    vars
        int a = 3, b = 6;
    
    print(multiply(multiply(a, a), multiply(b, b)));
}