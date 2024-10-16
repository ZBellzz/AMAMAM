Algoritmo "atv8_exercicio4"
// Disciplina   : UC3 ALGORITMOS
// Professor   : Mateus de Paula Pereira
// Descrição   : usuário para inserir um capital inicial, uma taxa de juros e o número de meses, e calcule o valor acumulado usando juros compostos. Exiba o saldo para cada mês até o final do período.
// Autor(a)    : Petrus Machado Ramos
// Data atual  : 16/10/2024
Var
// Seção de Declarações das variáveis
c, max, min, num: inteiro
nm: vetor[1..10] de inteiro

Inicio
// Seção de Comandos, procedimento, funções, operadores, etc...


//versao 4.0, é uma merda criar lista nessa merda, pro final ser apenas para enfeite
// sapoha é muito simples, pq perdi meu tempo fazendo apredendo fazer essa merda?


max <- -99999
min <- 999999

para c de 1 até 10 faça
     escreval("Informe um número:")
     leia(num)
     nm[c] <- num


     se num > max então
         max <- num
     fimse
     se num < min então
         min <- num
     fimse
fimpara

// gastei sanidade e tempo com algo simples so pra fazer algo bonito, desnecessario
escreval("Dos seguintes numeros")
para c de 1 ate 10 faca
     escreval(nm[c])
     
fimpara

escreval("O maior número é:", max)
escreval("O menor número é:", min)

Fimalgoritmo
