//Implementation of quick sort
pub fn quick_sort(arr: &mut Vec<i32>) {
    if arr.len() <= 1 {
        return;
    }
    let pivot = arr[0];
    let mut left = Vec::new();
    let mut right = Vec::new();
    for i in 1..arr.len() {
        if arr[i] < pivot {
            left.push(arr[i]);
        } else {
            right.push(arr[i]);
        }
    }
    quick_sort(&mut left);
    quick_sort(&mut right);
    left.push(pivot);
    left.append(&mut right);
    arr.clear();
    for i in 0..left.len() {
        arr.push(left[i]);
    }
}
