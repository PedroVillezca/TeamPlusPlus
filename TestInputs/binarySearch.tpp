program binarySearch;

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

main() {
    vars
        int i, value, result;
    print("VALUE:");
    read(value);
    from i=0 to 9 {
        arr[i] = i*5;
    }
    result = recursiveSearch(value, 0, 9);
    print("RESULT:");
    print(result);
}
