#ifndef HEAP_SORT_H
#define HEAP_SORT_H

template <typename T>
void swap(T &a, T &b) {
	T temp = a;
	a = b;
	b = temp;
}

template <typename T>
void heapify(T* arr, int n, int i) {
	int max = i;
	int left = 2 * i + 1;
	int right = 2 * i + 2;

	if (left < n && arr[left] > arr[max])
		max = left;

	if (right < n && arr[right] > arr[max])
		max = right;

	if (max != i) {
		swap(arr[i], arr[max]);
		heapify(arr, n, max);
	}

}

template <typename T>
void build_max_heap(T* arr, int n) {
	for (int i = n / 2 - 1; i >= 0; --i)
		heapify(arr, n, i);
}

template <typename T>
void heap_sort(T* arr, int n) {
	build_max_heap(arr, n);
	for (int i = n - 1; i > 0; --i) {
		swap(arr[0], arr[i]);
		heapify(arr, i, 0);
	}
}

#endif