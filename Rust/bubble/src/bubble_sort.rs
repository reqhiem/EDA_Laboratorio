//Implementation of Bubble Sort
pub fn bubble_sort(arr: &mut [i64]) {
    let mut i = 0;
    let mut j = 0;
    let mut temp = 0;
    let mut swapped = true;
    while swapped {
        swapped = false;
        i = 0;
        while i < arr.len() - 1 {
            j = i + 1;
            if arr[i] > arr[j] {
                temp = arr[i];
                arr[i] = arr[j];
                arr[j] = temp;
                swapped = true;
            }
            i += 1;
        }
    }
}
