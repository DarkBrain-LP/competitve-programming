#include <bits/stdc++.h>
using namespace std;

int main(){
    int a = 19, b = 7, n = 100, result = 0;
    cout << a/b << '\n';

    a = 10 * (a%b);

    for(int i = 0; i < n; i++){
        //result = 10*result + a/b;
        cout << a/b ;
        a = 10*(a%b);
    }

     cout << '\n';// << result << '\n';
}