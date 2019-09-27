#include <iostream>
#include <bits/stdc++.h>

using namespace std;
int main() {
    long double y1, y2;

    cout << "TABELA 1 -----------------------------------------------------" << endl;
    float lastStep1;
    for (float i = 0; i < 20.1; i+=0.1){
        cout << i << ": "<<exp(i) << endl;
        y1 = exp(i);
        lastStep1 = i;
    }

//    float step = 0.1;
//    float x1 = 0;
//    while (x1 < 20){
//        y1 = exp(x1);
//        cout << x1 << ": "<< y1 << endl;
//        x1 += step;
//    }

    cout << endl << "TABELA 2 -----------------------------------------------------" << endl;
    int lastStep2;
    for (int i = 0; i< 21; i++){
        cout << i << ": "<<exp(i) << endl;
        y2 = exp(i);
        lastStep2 = i;
    }

//    float step = 1;
//    float x2 = 0;
//    while (x2 < 20){
//        y2 = exp(x2);
//        cout << x2 << ": "<< y2 << endl;
//        x2 += step;
//    }



    /** O que está a acontecer?
     * um numero maquina é um numero que consegue representado na maquina sem perda
     * 0.1 não é um numero maquina no computador, porque este trabalha em base 2
     * estamos somar um número mais ou menos inferior a 0.1
     * logo y1 é um pouco menor do que devia
     * x = x0+n*passo ocorre menos erros, porque o erro não se multiplica
     * se o passo for um número maquina, todos os metodos funcionam bem
     */

    cout << endl;
    cout << "Equality: " << (y2 == y1) << endl;
    cout << "lastStep1: "<< lastStep1 << "; lastStep2: " << lastStep2 << endl;
    cout << "Equality of steps: " << (lastStep1 == lastStep2) << endl;


}


