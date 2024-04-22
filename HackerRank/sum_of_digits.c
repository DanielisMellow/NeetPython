#include <stdio.h>

int sum_of_digits(int num) {

  int sum = 0;

  while (num) {
    sum += (num % 10);

    num /= 10;
  }
  return sum;
}

int main() {

  int n;
  scanf("%d", &n);
  // Complete the code to calculate the sum of the five digits on n.
  printf("%d", sum_of_digits(n));
  return 0;
}
