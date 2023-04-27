#include "functions.h"
#include <iostream>

using namespace std;

void invertenome(char*nome){
    
   int i = tamanhode(nome);
   int j =0;
    while(j != i){
    cout<<nome[i-1];
    i--;
    }
}

int tamanhode(char*nome){
    
    int tamanho;
    for(int i =0; i<25;i++){
        if(nome[i] == '\0'){
        tamanho = i;
        break;
        }
    }
    return tamanho;
}