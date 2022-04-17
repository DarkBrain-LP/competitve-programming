#include <bits/stdc++.h>
using namespace std;

int factorial(int n){
    return (pow(1+sqrt(5), n) - (pow(1-sqrt(n), n))) / (pow(2,n)*sqrt(5));
}

int main(){
    cout << factorial(4);
}