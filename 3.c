#include <stdio.h>
#include <stdlib.h>
#include <time.h>

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
    int min = 0;
    int counter = 0;
    for (int i = 0; i < N - 1; i++) {
        if (2 * (array[i] + array[i + 1]) > max) {
            counter++;
            if ((array[i] + array[i + 1]) > min) {
                min = array[i] + array[i + 1];
            }
        }
    }
    printf("%d %d\n", counter, min);
    free(array);
}