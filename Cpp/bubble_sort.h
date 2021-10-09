#ifndef BUBBLE_SORT_H
#define BUBBLE_SORT_H

template <typename T>
void swap(T &a, T &b) {
	T temp = a;
	a = b;
	b = temp;
}

template <typename T>
void bubble_sort(T* arr, int n) {
	for (int i = 0; i < n - 1; ++i)
		for (int j = 0; j < n - i - 1; ++j)
			if (arr[j] > arr[j + 1])
				swap(arr[j], arr[j + 1]);
}

#endif