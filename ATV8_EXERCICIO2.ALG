Algoritmo "atv8_exercicio2"
// Disciplina   : UC3 ALGORITIMOS
// Professor   : Mateus de Paula Pereira
// Descri��o   : programa que pe�a ao usu�rio um n�mero inteiro positivo e verifique se ele � primo. Continue pedindo novos n�meros at� que o usu�rio insira um valor negativo.
// Autor(a)    : Petrus Machado Ramos
// Data atual  : 16/10/2024
Var
// Se��o de Declara��es das vari�veis 
nm : inteiro

Inicio
// Se��o de Comandos, procedimento, fun��es, operadores, etc... 

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