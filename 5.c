#include <stdlib.h>
#include <stdio.h>
#include <time.h>

#define N 5

int sum_line(int* array) {
    int sum = 0;
    for (int i = 0; i < N; i++) {
        sum += array[i];
    }
    return sum;
}

int main() {
    srand(time(NULL));
    int** array = (int**)malloc(N * sizeof(int*));
    for (int i = 0; i < N; i++) {
        array[i] = (int*)malloc(N * sizeof(int));
        for (int j = 0; j < N; j++) {
            array[i][j] = (rand() % (99 - 10 + 1)) + 10;
            printf("%d ", array[i][j]);
        }
        printf("\n");
    }

    printf("\n");

    if (sum_line(array[N - 1]) > sum_line(array[0])) {
        for (int i = 0; i < N; i++) {
            array[i][N - i - 1] *= 2;
        }
    }

    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            printf("%d ", array[i][j]);
        }
        printf("\n");
        free(array[i]);
    }
    free(array);
}
