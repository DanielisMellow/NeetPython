#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void print_freq(char *str, int size) {
  int *num_set = calloc(10, sizeof(int));

  for (int i = 0; i < size; i++) {
    if (str[i] >= '0' && str[i] <= '9') {
      num_set[str[i] - '0']++;
    }
  }

  for (int i = 0; i < 10; i++) {
    printf("%d ", num_set[i]);
  }
}
int main(int argc, char *argv[]) {

  char *s;
  s = malloc(1000 * sizeof(char));
  scanf("%[^\n]", s);

  print_freq(s, strlen(s));
  return EXIT_SUCCESS;
}
