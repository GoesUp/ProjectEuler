#include <stdio.h>
#include <stdlib.h>

int recursion(long long a, int *memo) {
    if (a < 100000002 && memo[a] != 0) {
        return memo[a];
    }

    if (a == 1) {
        memo[a] = 1;
        return 1;
    }

    if (a % 2 == 0) {
        int rez = 1 + recursion(a / 2, memo);
        if (a < 100000002) memo[a] = rez;
        return rez;
    }

    int rez = 1 + recursion(3 * a + 1, memo);
    if (a < 100000002) memo[a] = rez;
    return rez;
}

int main() {

    int *memo = (int *) calloc(100000002, sizeof(int));

    int maxNumber = 0;
    int maxValue = 0;

    for (int i = 1; i < 1e6; i++) {
        int vrednost = recursion(i, memo);
        if (vrednost > maxValue) {
            maxValue = vrednost;
            maxNumber = i;
        }
    }

    printf("%d\n", maxNumber);

    return 0;
}
