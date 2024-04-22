#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {

  char *s;
  s = malloc(1024 * sizeof(char));
  scanf("%[^\n]", s);
  s = realloc(s, strlen(s) + 1);
  // Write your logic to print the tokens of the sentence here.
  for (int i = 0; i < strlen(s) + 1; i++) {
    if (s[i] == ' ') {
      s[i] = '\n';
    }
  }
  printf("%s\n", s);

  return 0;
}
