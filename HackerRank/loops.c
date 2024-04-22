#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

static const char *nums[] = {"one", "two",   "three", "four", "five",
                             "six", "seven", "eight", "nine"};
int main() {
  int a, b;
  scanf("%d\n%d", &a, &b);
  // Complete the code.
  for (int i = a; i <= b; ++i) {
    if (i < 10) {
      printf("%s\n", nums[i - 1]);
    } else {
      (i % 2 == 0) ? printf("even\n") : printf("odd\n");
    }
  }
  return 0;
}
