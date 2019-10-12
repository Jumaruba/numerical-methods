#include <iostream>
#include <bits/stdc++.h>
#define MAX_ITER 10000
using namespace std;

long double f(long double);

// Prints root of func(x) in interval [a, b]
void regulaFalsi(double a, double b)
{
    if (f(a) * f(b) >= 0)
    {
        cout << "You have not assumed right a and b\n";
        return;
    }

    double c = a;  // Initialize result

    for (int i=0; i < MAX_ITER; i++)
    {
        // Find the point that touches x axis
        c = (a*f(b) - b*f(a))/ (f(b) - f(a));

        // Check if the above found point is root
        if (f(c)==0)
            break;

            // Decide the side to repeat the steps
        else if (f(c)*f(a) < 0)
            b = c;
        else
            a = c;
    }
    cout << "The value of root is : " << c;
}

long double f(long double a){
    return 1 + a + exp(a);
}
int main(){
    regulaFalsi(-2,1);
}
