program factorial;

vars
    int arr[91];

func int cyclicFactorial(int n) {
    vars
        int result = 1, i;
    
    from i=1 to n {
        result = result * i;
    }

    return(result);
}

func int recursiveFactorial(int n) {
    if (n == 0 or n == 1) {
        return(1);
    }
    return(n * recursiveFactorial(n - 1));
}

func int dynamicFactorial(int n) {   
    if (n == 0 or n == 1) {
        return(1);
    }

    if (arr[n] != -1) {
        return(arr[n]);
    }

    arr[n] = dynamicFactorial(n-1) * n;
    return(arr[n]);
}

main() {
    vars
        char option;
        int value, i;

    from i=0 to 90 {
        arr[i] = -1;
    }

    print("Cyclic, Recursive, or Dynamic?: ('c', 'r' or 'd'): ");
    read(option);
    print("Value: ");
    read(value);

    switch(option) {
        case 'c' {
            print(cyclicFactorial(value));
        }
        case 'r' {
            print(recursiveFactorial(value));
        }
        case 'd' {
            print(dynamicFactorial(value));
        }
        default {
            print("What?");
        }
    }  
}


