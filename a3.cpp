#include <iostream>
#include <omp.h>
#include <climits>
/*

The min_reduction function finds the minimum value in the input array using the #pragma omp parallel for
reduction(min: min_value) directive, which creates a parallel region and divides the loop iterations among the
available threads. Each thread performs the comparison operation in parallel and updates the min_value
variable if a smaller value is found.
1. Similarly, the max_reduction function finds the maximum value in the array, sum_reduction function finds the
sum of the elements of array and average_reduction function finds the average of the elements of array by
dividing the sum by the size of the array.
1. The reduction clause is used to combine the results of multiple threads into a single value, which is then
returned by the function. The min and max operators are used for the min_reduction and max_reduction
functions, respectively, and the + operator is used for the sum_reduction and average_reduction functions. In
the main function, it creates a vector and calls the functions min_reduction, max_reduction, sum_reduction, and
average_reduction to compute the values of min, max, sum and average respectively.
*/



using namespace std;

void min_reduction(int arr[], int n) {
    int min_value = INT_MAX;
    #pragma omp parallel for reduction(min: min_value)
    for (int i = 0; i < n; i++) {
        if (arr[i] < min_value) {
            min_value = arr[i];
        }
    }
    cout << "Minimum value: " << min_value << endl;
}

void max_reduction(int arr[], int n) {
    int max_value = INT_MIN;
    #pragma omp parallel for reduction(max: max_value)
    for (int i = 0; i < n; i++) {
        if (arr[i] > max_value) {
            max_value = arr[i];
        }
    }
    cout << "Maximum value: " << max_value << endl;
}

void sum_reduction(int arr[], int n) {
    int sum = 0;
    #pragma omp parallel for reduction(+: sum)
    for (int i = 0; i < n; i++) {
        sum += arr[i];
    }
    cout << "Sum: " << sum << endl;
}

void average_reduction(int arr[], int n) {
    int sum = 0;
    #pragma omp parallel for reduction(+: sum)
    for (int i = 0; i < n; i++) {
        sum += arr[i];
    }
    cout << "Average: " << (double)sum / n << endl;
}

int main() {
     int arr[] = {3, 1, 4, 1, 5, 9, 2, 6, 5, 3};
    int n = sizeof(arr) / sizeof(arr[0]);
    min_reduction(arr, n);
    max_reduction(arr, n);
    sum_reduction(arr, n);
    average_reduction(arr, n);

    return 0;
}
