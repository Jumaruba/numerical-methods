#include <iostream>
#include<bits/stdc++.h>

using namespace std;

long double f(long double i);

long double SB(float a, float b, float error){
    long double xAnt;
    int n = 1;
    long double x = (a+b)/2;
    if (f(a)*f(x) < 0) b = x;
    else a = x;

    do{
        //whats really important
        xAnt = x;
        x = (a+b)/2;    //new guess for the root
        if (f(a)*f(x) < 0) b = x;   //b is too large
        else a = x; //a is too large 

        cout <<"n: "<< n++ <<" |a :" << a << "|b: " << b <<"|x: " << x << "|f(a): " << f(a) << "|f(b): " << f(b) << endl;
    }while(abs(xAnt - x)> error );

    return x;
}

//the function 
long double f(long double x){
    //return -2.75*pow(i,3)+18*pow(i,2)-21*i-12;
    //9.3 e 9.5 | 0 e 0.2
    return x - 2*log(x)-5;
}
int main() {
    cout << SB(9.3,9.5, pow(10,-5)) << endl;
    return 0;
}
