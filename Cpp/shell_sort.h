#ifndef SHELL_SORT_H
#define SHELL_SORT_H

template <typename T>
void shell_sort(T* arr, int n) {
	for (int gap = n / 2; gap > 0; gap /= 2)
		for (int i = gap; i < n; ++i) {
			int key = arr[i];
			int j = i;
			while (j >= gap && arr[j - gap] > key) {
				arr[j] = arr[j - gap];
				j -= gap;
			}
			arr[j] = key;
		}
}

#endif