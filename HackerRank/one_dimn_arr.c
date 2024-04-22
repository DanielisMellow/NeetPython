#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int *create_arr(int size) {
  int *arr = (int *)malloc(sizeof(int) * size);

  return arr;
}

int sum_arr(int *arr, int size) {
  int sum = 0;

  for (int i = 0; i < size; i++) {
    sum += arr[i];
  }
  return sum;
}

int main() {

  int n;
  scanf("%d", &n);
  int *arr = create_arr(n);

  if (arr == NULL) {

    exit(EXIT_FAILURE);
  }

  for (int i = 0; i < n; i++) {
    scanf("%d", &arr[i]);
  }
  printf("%d", sum_arr(arr, n));
  return 0;
}
