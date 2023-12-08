#include <stdio.h>
#include <limits.h>

int sum_numbers(int num) {
    int sum = 0;
    int last_digit = 0;
    while (num > 0) {
        int last_digit = num % 10;
        sum += last_digit;
        num /= 10;
    }
    return sum;
}


int main() {
    int min = INT_MAX;
    int counter = 0;
    for (int num = 123456; num < 234567; num++) {
        if (num % sum_numbers(num) == 0) {
            counter++;
            if (num < min) {
                min = num;
            }
        }
    }

    printf("%d %d\n", counter, min);
}