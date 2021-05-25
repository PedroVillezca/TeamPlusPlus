program fibo;

vars
    int arr[50];

func int cyclicFibonacci(int n) {
    vars
        int prev = 0, curr = 1, next, i;
    
    if (n == 0 or n == 1) {
        return(n);  
    }

    from i=2 to n {
        next = curr + prev;
        prev = curr;
        curr = next;
    }

    return(next);
}

func int recursiveFibonacci(int n) {
    if (n == 0 or n == 1) {
        return(n);
    }

    return(recursiveFibonacci(n - 2) + recursiveFibonacci(n - 1));
}

func int dynamicFibonacci(int n) {
    if (n == 0 or n == 1) {
        return(n);
    }

    if (arr[n] != -1) {
        return(arr[n]);
    }

    arr[n] = dynamicFibonacci(n-2) + dynamicFibonacci(n-1);
    return(arr[n]);
}

main() {
    vars
        char option;
        int value, i;

    from i=0 to 49 {
        arr[i] = -1;
    }

    print("Cyclic, Recursive, or Dynamic?: ('c', 'r' or 'd'): ");
    read(option);
    print("Value: ");
    read(value);

    switch(option) {
        case 'c' {
            print(cyclicFibonacci(value));
        }
        case 'r' {
            print(recursiveFibonacci(value));
        }
        case 'd' {
            print(dynamicFibonacci(value));
        }
        default {
            print("What?");
        }
    }   
}