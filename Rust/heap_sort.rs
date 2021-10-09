//Implementation of Heap Sort

fn heapify(arr: &mut [i32], n: usize, i: usize) {
    let mut largest = i;
    let mut l = 2 * i + 1;
    let mut r = 2 * i + 2;

    if l < n && arr[l] > arr[largest] {
        largest = l;
    }

    if r < n && arr[r] > arr[largest] {
        largest = r;
    }

    if largest != i {
        arr.swap(i, largest);
        heapify(arr, n, largest);
    }
    return;
}


pub fn heap_sort(arr: &mut [i32]) {
    let mut n = arr.len();
    for i in (0..n).rev() {
        heapify(arr, n, i);
    }
    for i in (0..n).rev() {
        arr.swap(0, i);
        heapify(arr, i, 0);
    }
}