#include <stdio.h>
// Complete the following function.

void calculate_the_maximum(int n, int k) {
  // Write your code here.
  int max_and = 0;
  int max_or = 0;
  int max_xor = 0;

  int temp_max_and = 0;
  int temp_max_or = 0;
  int temp_max_xor = 0;
  for (int a = 1; a < n; a++) {

    for (int b = a + 1; b <= n; b++) {
      temp_max_and = (a & b);
      temp_max_or = (a | b);
      temp_max_xor = (a ^ b);
      if ((temp_max_and > max_and) && (temp_max_and < k)) {
        max_and = temp_max_and;
      }
      if ((temp_max_or > max_or) && (temp_max_or < k)) {
        max_or = temp_max_or;
      }
      if ((temp_max_xor > max_xor) && (temp_max_xor < k)) {
        max_xor = temp_max_xor;
      }
    }
  }
  printf("%d\n%d\n%d\n", max_and, max_or, max_xor);
}

// Complete the following function.
void calculate_the_maximumV2(int n, int k) {
  // Write your code here.
  int maxAnd = 0;
  int maxOr = 0;
  int maxXor = 0;

  for (int i = 1; i <= n; i++) {
    for (int j = i + 1; j <= n; j++) {

      printf("%d & %d = %d\n", i, j, i & j);
      printf("%d | %d = %d\n", i, j, i | j);
      printf("%d ^ %d = %d\n", i, j, i ^ j);
      printf("\n");
      if (((i & j) > maxAnd) && ((i & j) < k)) {
        maxAnd = i & j;
      }
      if (((i | j) > maxOr) && ((i | j) < k)) {
        maxOr = i | j;
      }
      if (((i ^ j) > maxXor) && ((i ^ j) < k)) {
        maxXor = i ^ j;
      }
    }
  }
  printf("%d\n%d\n%d\n", maxAnd, maxOr, maxXor);
}

int main() {
  int n, k;

  scanf("%d %d", &n, &k);
  calculate_the_maximum(n, k);

  return 0;
}
