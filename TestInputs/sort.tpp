program sort;

vars
    int arr[10];

func void swap(int i, int j) {
    vars
        int temp;
    
    temp = arr[i];
    arr[i] = arr[j];
    arr[j] = temp;
}

func void bubbleSort(int lim) {
    vars
        int temp, i, j;
    
    from i=0 to lim-1 {
        from j=0 to lim - i - 2 {
            if (arr[j] > arr[j+1]) {
                swap(j, j+1);
            }
        }
    }
}

func int partition(int low, int high) {
    vars
        int pivot = arr[high];
        int i = low - 1, j;

    from j=low to high-1 {
        if (arr[j] < pivot) {
            i = i + 1;
            swap(i, j);
        }
    }
    swap(i+1, high);
    return(i + 1);
}

func void quickSort(int low, int high) {
    vars
        int pivot;
    if (low < high) {
        pivot = partition(low, high);

        quickSort(low, pivot - 1);
        quickSort(pivot + 1, high);
    }
}

main() {
    vars
        int i;
    from i = 0 to 9 {
        read(arr[i]);
    }

    # bubbleSort(10);
    quickSort(0, 9);

    print("Result:");
    from i = 0 to 9 {
        print(arr[i]);
    }
}