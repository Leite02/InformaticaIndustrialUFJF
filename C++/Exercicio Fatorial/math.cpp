float potencia(float b, int exp)
{
	float r = b;
	for(int i=1;i<exp;i++)
	{
		r *=b;
	}
	return r;
}

int fatorial(int a){
    int fatorial = 1;
    for(int r = a; r>0 ; r--){
        fatorial *= r;
    }
    return fatorial;

}

float funcao (float b){
   float x = b;
   
   float y;
   
   y = fatorial(5)*potencia(x,3) + fatorial(4)*potencia(x,2)+fatorial(3)*x + fatorial(2);
  
  return y;
}