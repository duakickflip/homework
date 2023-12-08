#include <stdlib.h>
#include <stdio.h>
#include <time.h>

#define N 6
#define M 6

int** generate_array(int min, int max) {
    int** array = (int**)malloc(N * sizeof(int*));
    for (int i = 0; i < N; i++) {
        array[i] = (int*)malloc(M * sizeof(int));
        for (int j = 0; j < M; j++) {
            array[i][j] = (rand() % (max - min + 1)) + min;
        }
    }
    return array;
}

void print_array(int** array) {
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < M; j++) {
            printf("%d ", array[i][j]);
        }
        printf("\n");
    }
}

void free_array(int** array) {
    for (int i = 0; i < N; i++) {
        free(array[i]);
    }
    free(array);
}

int main() {
    int** array = generate_array(10, 99);
    print_array(array);
    for (int i = 0; i < N - 1; i += 2) {
        int* buffer = array[i];
        array[i] = array[i + 1];
        array[i + 1] = buffer;
    }
    printf("\n");
    print_array(array);
    free_array(array);
}