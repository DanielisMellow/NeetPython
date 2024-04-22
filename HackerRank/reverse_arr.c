#include <stdio.h>
#include <stdlib.h>

void swap(int *x, int *y) {
  int a = *x;
  *x = *y;
  *y = a;
}

void reverse_arr(int *arr, int size) {

  int i = 0;
  int j = size - 1;

  while (i < j) {
    swap(&arr[i], &arr[j]);
    i++;
    j--;
  }
}

int main() {
  int num, *arr, i;
  scanf("%d", &num);
  arr = (int *)malloc(num * sizeof(int));
  for (i = 0; i < num; i++) {
    scanf("%d", arr + i);
  }

  reverse_arr(arr, num);
  for (i = 0; i < num; i++)
    printf("%d ", *(arr + i));
  return 0;
}
