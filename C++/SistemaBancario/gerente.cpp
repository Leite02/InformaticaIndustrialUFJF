#include "gerente.h"
#include <iostream>
#include <string>

using namespace std;

Gerente::Gerente()
{
    this->senha = 1111;
    this->numero = 0;
    this->nome = "Nenhum";
}

Gerente::Gerente(int senha, int numero, string nome)
{
    this->senha = senha;
    this->numero = numero;
    this->nome = nome;
}

Gerente::~Gerente()
{
}

void Gerente::exibeDados()
{
    std::cout<< "Nome: "<<this->nome<<std::endl;
    std::cout<< "Numero: "<<this->numero<<std::endl;
}

void Gerente::setSenha(int novaSenha)
{
    this->senha = novaSenha;
}

bool Gerente::validaSenha(int senha)
{
return (this->senha == senha);
}
