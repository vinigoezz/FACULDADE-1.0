d1 = int(input('Digite o primeiro dígito do CPF: '))
d2 = int(input('Digite o segundo dígito do CPF: '))
d3 = int(input('Digite o terceiro dígito do CPF: '))
d4 = int(input('Digite o quarto dígito do CPF: '))
d5 = int(input('Digite o quinto dígito do CPF: '))
d6 = int(input('Digite o sexto dígito do CPF: '))
d7 = int(input('Digite o sétimo dígito do CPF: '))
d8 = int(input('Digite o oitavo dígito do CPF: '))
d9 = int(input('Digite o nono dígito do CPF: '))

# Calculo do primeiro dígito verificador
calculo = d1 * 10 + d2 * 9 + d3 * 8 + d4 * 7 + d5 * 6 + d6 * 5 + d7 * 4 + d8 * 3 + d9 * 2
digito1 = calculo * 10 
verificador1 = digito1 % 11
if verificador1 == 10:
    verificador1 = 0

# Calculo do segundo dígito verificador
calculo2 = d1 * 11 + d2 * 10 + d3 * 9 + d4 * 8 + d5 * 7 + d6 * 6 + d7 * 5 + d8 * 4 + d9 * 3 + digito1 * 2
digito2 = calculo2 * 10 
verificador2 = digito2 % 11
if verificador2 == 10:
    verificador2 = 0

print(f'Os digitos do CPF são: {d1}{d2}{d3}{d4}{d5}{d6}{d7}{d8}{d9}-{verificador1}{verificador2}')
