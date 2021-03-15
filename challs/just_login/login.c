#include <stdio.h>
#include <string.h>

int main() {
  char pass[256];
  int key = 0x55;
  int flag[] = {33, 48, 63, 54, 33, 51, 46, 61, 52, 39, 49, 54, 58, 49, 48, 49, 10, 37, 52, 38, 38, 34, 58, 39, 49, 38, 10, 49, 58, 59, 33, 10, 51, 58, 58, 57, 10, 56, 48, 40};
  
  printf("Enter the password: ");
  if (fgets(pass, sizeof(pass), stdin) != NULL) {
    if (strcmp(pass, "nobody_will_guess_this_password_its_far_too_long\n") == 0) {
      printf("Good job! Have the flag: ");
      for (int i = 0; i < sizeof(flag)/sizeof(int); ++i) {
	printf("%c", flag[i] ^ key);
      }
      printf("\n");
    }
    else {
      printf("Wrong password! Goodbye.\n");
    }
  }
}
