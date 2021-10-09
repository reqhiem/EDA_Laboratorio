//Implementation of selection sort
pub fn shell_sort(arr: &mut [i32]) {
    let mut h = 1;
    while h < arr.len() / 3 {
        h = 3 * h + 1;
    }
    while h >= 1 {
        for i in h..arr.len() {
            let mut j = i;
            while j >= h && arr[j] < arr[j - h] {
                arr.swap(j, j - h);
                j -= h;
            }
        }
        h /= 3;
    }
}
