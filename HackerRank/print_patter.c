#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// 5 5 5 5 5 5 5 5 5
// 5 4 4 4 4 4 4 4 5
// 5 4 3 3 3 3 3 4 5
// 5 4 3 2 2 2 3 4 5
// 5 4 3 2 1 2 3 4 5
// 5 4 3 2 2 2 3 4 5
// 5 4 3 3 3 3 3 4 5
// 5 4 4 4 4 4 4 4 5
// 5 5 5 5 5 5 5 5 5

void check(int i, int j, int first, int last, int num) {
  if (num < 1) {
    return;
  }

  if (i == first || i == last || j == first || j == last) {
    printf("%d ", num);
  } else {
    check(i, j, first + 1, last - 1, num - 1);
  }
}

void print_pattern(int num) {
  int x = num + (num - 1);

  for (int i = 0; i < x; i++) {
    for (int j = 0; j < x; j++) {
      check(i, j, 0, x - 1, num);
    }
    printf("\n");
  }
}

int main() {

  int n;
  scanf("%d", &n);
  // Complete the code to print the pattern.
  printf("\n");
  print_pattern(n);
  return 0;
}
