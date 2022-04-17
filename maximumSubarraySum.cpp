#include <bits/stdc++.h>
using namespace std;

int maxSubarraySumOn(int array[], int n){

    int best = 0, sum = 0;
    for (int k = 0; k < n; k++) {
    sum = max(array[k],sum+array[k]);
    best = max(best,sum);
    }
    cout << best << "\n";
}

int maxSubarraySumOn2(int array[], int n){

    int best = 0;
    for (int a = 0; a < n; a++) {
        int sum = 0;
        for (int b = a; b < n; b++) {
            sum += array[b];
            best = max(best,sum);
        }
    }
    cout << best << "\n";
}

int maxSubarraySumOn3(int array[], int n){

    int best = 0;
    for (int a = 0; a < n; a++) {
        for (int b = a; b < n; b++) {
            int sum = 0;
            for (int k = a; k <= b; k++) {
                sum += array[k];
            }
            best = max(best,sum);
        }
    }
    cout << best << "\n";
}