program cycles;

vars
    int arr[3,3];

main() {
    vars
        int i, j;

    from i=0 to 2 {
        from j=0 to 2 {
            arr[i, j] = (i+1) * (j+1);
        }
    }

    i = 0;
    while(i <= 2) {
        j = 0;
        while(j <= 2) {
            print(arr[i, j], "\t");
            j = j+1;
        }
        print("\n");
        i = i+1;
    }
}