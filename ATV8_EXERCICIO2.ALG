Algoritmo "atv8_exercicio2"
// Disciplina   : UC3 ALGORITIMOS
// Professor   : Mateus de Paula Pereira
// Descrição   : programa que peça ao usuário um número inteiro positivo e verifique se ele é primo. Continue pedindo novos números até que o usuário insira um valor negativo.
// Autor(a)    : Petrus Machado Ramos
// Data atual  : 16/10/2024
Var
// Seção de Declarações das variáveis 
nm : inteiro

Inicio
// Seção de Comandos, procedimento, funções, operadores, etc... 

enquanto verdadeiro faca
         escreval("Digite um numero inteiro positivo ")
         leia(nm)
         
         se nm < 0 entao
            escreval("numero negativo")
            interrompa
         senao
               se nm < 2 entao
                  escreval("nao primo ")

               senao
                    se (nm = 2) ou (nm = 3) entao
                       escreval("numero primo")
                       
                    senao
                         se (nm % 2 = 0) ou (nm % 3 = 0)entao
                            escreval("numero n primo")
                         senao
                              escreval("numero primo")
                         fimse
                    
                    fimse


               fimse
         fimse





fimenquanto



Fimalgoritmo