#include <iostream>
#include<bits/stdc++.h>

using namespace std;

long double f(long double i);

long double SB(float a, float b, float error){
    long double x = 0;
    int n = 1;
    do{
        //whats really important
        x = (a+b)/2;    //new guess for the root
        if (f(a)*f(x) < 0) b = x;   //b is too large
        else a = x; //a is too large
        cout <<"n:\t"<< n++ <<"\t" <<"|a:\t" << a <<"\t"<< "|b:\t" << b <<"\t"<<"|x:\t" << x <<"\t"<< "|f(a):\t" << f(a) <<"\t"<< "|f(b):\t" << f(b) <<"\t"<< endl;
    }while(abs(a-b)> error );

    return x;
}

long double f(long double x){
    //return -2.75*pow(i,3)+18*pow(i,2)-21*i-12;
    //9.3 e 9.5 | 0 e 0.2
    //return x - 2*log(x)-5;
    //0.2 e 0.3| 98 e 100
    return exp(0.7*x-pow(x,2)-0.5);
}
int main() {
    cout << SB(-1,0, pow(10,-5)) << endl;
    return 0;
}
