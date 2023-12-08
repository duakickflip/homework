#include <stdlib.h>
#include <stdio.h>
#include <time.h>

#define N 1000

int main() {
    int counter = 0;
    srand(time(NULL));
    int* array = (int*)malloc(N * sizeof(int));
    for (int i = 0; i < N; i++) {
        array[i] = rand() % 15001;
        printf("%d ",array[i]);
        if (array[i] % 2 == 0 && array[i] % 3 != 0) {
            counter++;
        }
    }
    printf("\n");

    for (int i = 0; i < N; i++) {
        if (array[i] % 2 != 0 && array[i] % 3 == 0) {
            array[i] = counter;
        }
        printf("%d ", array[i]);
    }
    printf("\n");

    free(array);
}