program factorial;

vars
    int arr[91];

func int factorial(int n) {   
    vars
        int temp;
        
    if (n == 0 or n == 1) {
        return(1);
    }

    if (arr[n] != -1) {
        # print("HELLO");
        return(arr[n]);
    }

    arr[n] = factorial(n-1) * n;

    # print(arr[n]);
    return(arr[n]);
}

main() {
    vars
        int i, continue = 1, num, result;
    
    from i=0 to 90 {
        arr[i] = -1;
    }

    from i=0 to 9 {
        print(arr[i]);
    }

    while(continue) {
        print("Number:");
        read(num);
        result = factorial(num);
        print("VERIFY");
        from i=0 to 9 {
            print(arr[i]);
        }
        print("VERIFY");
        print("Result:", result);
        print("Continue? 0 or 1.");
        read(continue);
    }
}


