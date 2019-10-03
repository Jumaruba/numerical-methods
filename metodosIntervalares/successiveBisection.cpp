#include <iostream>
#include <bits/stdc++.h> 

using namespace std;

long double f(long double);

long double BS(){
    long double low = -2, high = 1, mid = 1, midAnterior, error = 5*1e-3;

    do{
        midAnterior = mid;
        mid = (high+low)/2;
        if (f(mid)*f(low) < 0) high = mid;
        else low = mid;
    }while(abs(mid-midAnterior) > error);
    return mid;
}

long double f(long double a){
    return 1 + a + exp(a);
}
int main(){
    cout << BS() << endl;
}
