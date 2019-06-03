#include <stdio.h>

int recursion(int a, int b, int max) {
    if (b > max) return 0;
    if (b % 2 == 0) return b + recursion(b, a + b, max);
    return recursion(b, a + b, max);
}

int main() {
    printf("%d\n", recursion(1, 1, 4e6));
    return 0;
}
