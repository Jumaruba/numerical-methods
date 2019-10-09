#include <bits/stdc++.h>

using namespace std; 


//we wanna find the root for x^3+4 = 0; 


float f(float x){return x^3+4;}
float df(float x){return 3*x^2;}

float newtonMethod(float guess, int iter){
	x = guess; 

	for (int i = 0; i < iter; i++)
		x = x - f(x)/df(x); 

	return x; 
}


int main(){
	cout << fixed << set.precision(6); 

	cout << newtonMethod(1.4, 14);
}