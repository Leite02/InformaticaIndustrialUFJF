#include <iostream>
#include "math.h"

using namespace std;

int main()
{
    float x1,x2,x3,y1,y2,y3;
    x1 = 25;
    x2 = fatorial(7);
    x3 = potencia(2.5,3);
    
    y1= funcao(x1);
    y2 = funcao(x2);
    y3 = funcao(x3);
    
    cout<<"y(3) = ";cout<<y1<<endl;
    cout<<"y(3!) = ";cout<<y2<<endl;
    cout<<"y(2^3) = ";cout<<y3<<endl;
    
    
    system("pause");
    return 0;
}