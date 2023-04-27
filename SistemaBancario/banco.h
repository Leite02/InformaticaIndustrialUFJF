#ifndef BANCO_H
#define BANCO_H

#include "conta.h"
#include "gerente.h"
#include <string>


#define NUMGERENTES 5

class Banco
{
private:
    
    Conta* pContas;
    Conta* pcopiaContas;
    
    Gerente gerentes[NUMGERENTES];
    int numeroAtualdeContas;
public:
    Banco();
    ~Banco();
    Conta* buscaConta(int numero); 
    Gerente* buscaGerente(int numero);
    void atendimento();
    void atendimentoCliente();
    void atendimentoGerente();
    int getNumeroAtualContas(int senha,Gerente* contagerente);
    void criaContaNova(int senha, Gerente* contaGerente);
};


#endif
