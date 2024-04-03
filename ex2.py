peso = float(input('Qual seu peso? (kg)'))
altura = float(input('Qual sua altura?(m)'))
imc = peso / (altura ** 2)
print('o IMC dessa pessoa é {:.2f}'.format(imc))
if imc < 18.5:
    print('CLASSIFICACAO: Abaixo do peso')
elif imc >= 18.5 and imc < 25:
    print('CLASSIFICACAO: Peso ideal')
elif imc >25 and imc <30:
    print('CLASSFICACAO: Sobrepeso')
elif imc >30 and imc < 40:
    print('CLASSIFICACAO: Obesidade')
else:
    print('CLASSIFICACAO: Thais carla')