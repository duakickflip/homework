#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <limits.h>

#define N 10

int main() {
    int max = 0;
    srand(time(NULL));
    int* array = (int*)malloc(N * sizeof(int));
    for (int i = 0; i < N; i++) {
        array[i] = rand() % 10001;
        printf("%d ", array[i]);
        if (array[i] > max && array[i] % 3 == 0) {
            max = array[i];
        }
    }
    printf("\n");
    int min = INT_MAX;
    int counter = 0;
    for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                if (i == j) {
                    continue;
                }
                if (2 * (array[i] + array[j]) > max) {
                    counter++;
                    if (array[i] + array[j] < min) {
                        min = array[i] + array[j];
                    }
                }
            }
    }
    printf("%d %d\n", counter, min);
    free(array);
}