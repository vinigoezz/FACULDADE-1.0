#Tendo como dados de entrada a altura e o sexo de uma pessoa, implemente um
#programa que calcule seu peso ideal, utilizando as seguintes fórmulas:
#• para homens: (72.7 * h) – 58;
#• para mulheres: (62.1 * h) – 44.7. 
altura = float(input('digite sua altura'))
sexo = str(input('Digite seu sexo [M/F]: ')).strip().upper()[0]
peso_ideal_M = (72.7 * altura) - 58
peso_ideal_F = (62.1 * altura) - 44.7
if sexo in 'Mm':
    print(f'Seu peso ideal é {peso_ideal_M:.2f}')
elif sexo in 'Ff':
    print(f'Seu peso ideal é {peso_ideal_F:.2f}')
else:
    print('Comando inválido')
