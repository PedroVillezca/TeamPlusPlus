program search;

vars
    int arr[10], mid;

func int binarySearch(int value) {
    vars
        int start = 0;
        int end = 9;

    while(start <= end) {
        mid = (end + start) / 2;
        
        if (arr[mid] == value) {
            return(mid);
        } elif (arr[mid] > value) {
            end = mid - 1;
        } else {
            start = mid + 1;
        }
    }
    
    return(-1);
}

func int recursiveSearch(int value, int start, int end) {
    if (start <= end) {
        mid = (end + start) / 2;
        
        if (arr[mid] == value) {
            return(mid);
        } elif (arr[mid] > value) {
            return(recursiveSearch(value, start, mid-1));
        } else {
            return(recursiveSearch(value, mid+1, end));
        }
    }
    
    return(-1);
}

func int linearSearch(int value) {
    vars
        int i;
    
    from i=0 to 9 {
        if (arr[i] == value) {
            return(i);
        }
    }

    return (-1);
}

main() {
    vars
        int i, value, result;
        char option;
        
    from i=0 to 9 {
        read(arr[i]);
    }
    print("Iterative Binary Search, Recursive Binary Search or Linear Search? ('i', 'r', or 'l'): ");
    read(option);
    print("Value to search: ");
    read(value);
    
    switch(option) {
        case 'i' {
            print(binarySearch(value));
        }
        case 'r' {
            print(recursiveSearch(value, 0, 9));
        }
        case 'l' {
            print(linearSearch(value));
        }
        default {
            print("What? \n");
        }
    }
}
