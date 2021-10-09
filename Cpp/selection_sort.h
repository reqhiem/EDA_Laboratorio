#ifndef SELECTION_SORT_H
#define SELECTION_SORT_H

template <typename T>
void swap(T &a, T &b) {
	T temp = a;
	a = b;
	b = temp;
}

template <typename T>
void selection_sort(T* arr, int n) {
	for (int i = 0; i < n - 1; ++i) {
		int min_index = i;
		for (int j = i + 1; j < n; ++j)
			if (arr[j] < arr[min_index])
				min_index = j;
		swap(arr[min_index], arr[i]);
	}
}

#endif