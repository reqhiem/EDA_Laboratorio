#ifndef MERGE_SORT_H
#define MERGE_SORT_H

template <typename T>
void merge(T* arr, int l, int m, int r) {
	int n1 = m - l + 1;
	int n2 = r - m;

	T *L = new T[n1];
	T *R = new T[n2];

	for (int i = 0; i < n1; ++i)
		L[i] = arr[l + i];
	for (int j = 0; j < n2; ++j)
		R[j] = arr[m + 1 + j];

	int i = 0, j = 0, k = l;

	while (i < n1 && j < n2) {
		if (L[i] <= R[j]) {
			arr[k] = L[i];
			++i;
		}
		else {
			arr[k] = R[j];
			++j;
		}
		++k;
	}

	while (i < n1) {
		arr[k] = L[i];
		++i;
		++k;
	}

	while (j < n2) {
		arr[k] = R[j];
		++j;
		++k;
	}

	delete[] L;
	delete[] R;
}

template <typename T>
void merge_sort(T* arr, int l, int r) {
	if (l < r) {
		int m = l + (r - l) / 2;

		merge_sort(arr, l, m);
		merge_sort(arr, m + 1, r);

		merge(arr, l, m, r);
	}
}

#endif