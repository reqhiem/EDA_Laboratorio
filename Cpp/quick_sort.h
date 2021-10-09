#ifndef QUICK_SORT_H
#define QUICK_SORT_H

template <typename T>
int partition(T* arr, int low, int high) {
	int pivot = arr[high];
	int i = (low - 1);

	for (int j = low; j <= high - 1; ++j)
		if (arr[j] < pivot) {
			++i;
			swap(arr[i], arr[j]);
		}
	swap(arr[i + 1], arr[high]);

	return (i + 1);
}

template <typename T>
void quick_sort(T* arr, int low, int high) {
	if (low < high) {
		int pi = partition(arr, low, high);

		quick_sort(arr, low, pi - 1);
		quick_sort(arr, pi + 1, high);
	}
}

#endif