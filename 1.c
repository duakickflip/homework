#include <stdio.h>

int main() {
    int array[] = {7, 13, 17, 19};
    int counter, num_counter, sum;
    for (int num = 25000; num < 35000; num++) {
        counter = 0;
        for (int i = 0; i < 4; i++) {
            if (num % array[i] == 0) {
                counter++;
            }
        }
        if (counter == 2) {
            num_counter++;
            sum += num;
        }
    }
    printf("%d %d\n", num_counter, sum);
}