#ifndef GERENTE_H
#define GERENTE_H

#include <string>


class Gerente
{

private:
    int senha;

public:
    Gerente();
    ~Gerente();
    Gerente(int senha, int numero, std::string nome);
    int numero;
    std::string nome;
    void setSenha(int novaSenha);
    bool validaSenha(int senha);
    void exibeDados();
    
};
#endif
