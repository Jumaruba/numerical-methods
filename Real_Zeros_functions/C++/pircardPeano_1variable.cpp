#include <bits/stdc++.h>

using namespace std; 


//queremos achar a raiz de f(x) = x+1-tan(x)
//reformulando ficamos: 
//0 = x+1-tan(x)
//tan(x) = x+1
//x = atan(x+1)

double f(double x){return atan(x+1);}

void picardPeano(double x0, unsigned int num_iter){
	double x = x0; 

	for (unsigned int i = 1; i <=num_iter; i++){
		x = f(x); 
		//print current value
		cout << i << ":\t" << x << endl;
	}
}

int main(){
	cout << fixed; 
	cout.precision(6); 

	//guess
	const double x0 = 1.1; 

	picardPeano(x0,8); 
	return 0; 
}