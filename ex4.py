'''Implemente um programa que calcule o que deve ser pago por um produto,
considerando o preço normal de etiqueta e a escolha da condição de pagamento. Utilize
os códigos da tabela a seguir para ler qual a condição de pagamento escolhida e efetuar o
cálculo adequado.
Código Condição de pagamento
• 1 – À vista em dinheiro ou cheque, recebe 10% de desconto
• 2 – À vista no cartão de crédito, recebe 15% de desconto
• 3 – Em duas vezes, preço normal de etiqueta sem juros
• 4 – Em duas vezes, preço normal de etiqueta mais juros de 10%'''
produto = float(input('Preço do produto: '))
print('''OPÇÔES DE PAGAMENTO:
    [1] À vista em dinheiro ou cheque, com 10% de desconto
    [2] À vista no cartão de crédito, com 15% de desconto
    [3] Em duas vezes, preço normal de etiqueta sem juros
    [4] Em duas vezes, preço normal de etiqueta mais juros de 10%''')
opção = int(input('Escolha uma das opções acima: '))
if opção == 1:
    desconto = produto - (produto * 10 / 100)
    print(f'O valor final da sua compra com 10% de desconto é {desconto:.2f} R$')
elif opção == 2:
    desconto = produto - (produto * 15 / 100)
    print(f'O valor final da sua compra com 15% de desconto é {desconto:.2f} R$')
elif opção == 3:
    print(f'Sua compra em 2x será sem juros e preço normal. no valor de {produto}')
elif opção == 4:
    juros = produto + (produto * 10/100)
    print(f'Sua compra em 2x será COM JUROS na porcentagem de 10% no preço da etiqueta. valor de {juros:.2f} R$')
else:
    print('opção inválida.')


                