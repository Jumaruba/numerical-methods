#include <iostream>
#include <bits/stdc++.h>


using namespace std;

long double sucessiveBisection(long double number, long double step) {
    long double low = 0, high = number, mid;
    while (high >= low) {
        mid = (low + high) / 2;
        if (((mid - step) * (mid - step)) < number && (mid * mid) >= number) return mid;
        if (((mid) * (mid)) > number) high -= step;
        else if (((mid) * (mid)) > number) low+= step;
    }
    return mid;
}

int main() {
    int numero = 9;
//    long double resultado = 0;
//    float step = 0.0001;
//    for (double i = 1; i <= numero * 10 * 10 * 10 * 10 / 2; i += 1) {
//        if ((i * step) * (i * step) >= numero && ((i - 1) * step) * ((i - 1) * step) < numero) {
//            resultado = i * step;
//            break;
//        }
//    }

//fazer abs(x*x-a <= precisao)
    cout << sucessiveBisection(numero, 0.0001);


}

