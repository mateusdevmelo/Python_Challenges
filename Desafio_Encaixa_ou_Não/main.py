"""
Desafio
Paulinho tem em suas mãos um novo problema. Agora a sua professora lhe pediu que construísse um programa para verificar,
à partir de dois valores muito grandes A e B, se B corresponde aos últimos dígitos de A.

Entrada
A entrada consiste de vários casos de teste. A primeira linha de entrada contém um inteiro N que indica a quantidade de casos de teste.
Cada caso de teste consiste de dois valores A e B maiores que zero, cada um deles podendo ter até 1000 dígitos.

Saída
Para cada caso de entrada imprima uma mensagem indicando se o segundo valor encaixa no primeiro valor, confome exemplo abaixo.

 
Exemplo de Entrada	Exemplo de Saída
4
56234523485723854755454545478690 78690
5434554 543
1243 1243
54 64545454545454545454545454545454554

encaixa
nao encaixa
encaixa
nao encaixa
"""


n = int(input())  # primeiro número que entra é o '4' que é a quantidade de loops que deve ser feito

while n > 0:
    N = input().split(" ")  # aqui onde o número será inserido e separados numa lista


    A = N[0]  # item com indice 0 da lista
    B = N[1]  # item com indice 1 da lista

    b = -len(B)  # iremos reservar o tamanho do item B

    if (0<len(A)<=1000) and (0<len(B)<=1000): #checaremos se o tamanho dos itens está dentro do permitido

      if len(A) >= len(B):     # checaremos se o tamanho de A é maior que B

          if A[b:] == B:       # iremos comparar se o final de A é igual o número B
              print('encaixa')
          else:
              print('nao encaixa')
      else:
          print('nao encaixa')
      
      n -= 1