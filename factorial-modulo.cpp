#include <bits/stdc++.h>
using namespace std;
int main() {
// solution comes here
    int n = 152036, m = 120;
    long long x = 1;
    for (int i = 2; i <= n; i++) {
        x = (x*i)%m;
    }
    cout << x%m << "\n";
}