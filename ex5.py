'''Implemente um programa que leia o destino do passageiro, se a viagem inclui retorno
(ida e volta) e informar o preço da passagem conforme a tabela a seguir:
Condição Ida Ida e volta
Região Norte R$ 500,00 R$ 900,00
Região Nordeste R$ 350,00 R$ 650,00
Região Centro-Oeste R$ 350,00 R$ 600,00
Região Sul R$ 300,00 R$ 550,00''' 
titulo = 'Viagens'
print('-=' * 10)
print(titulo.center(20))
print('-=' * 10)
destinoresp = str(input('Qual seria seu destino? ')).strip()
ida_volta = str(input('Ida ou ida e volta? ')).strip()
destinos = ['Região Norte', 'Região Nordeste', 'Região Centro - Oeste', 'Região Sul']
respidavolta = ['ida', 'ida e volta']
if destinoresp not in destinos and ida_volta not in respidavolta:
    print('Opção inválida.')
if destinoresp == 'Região Norte' and ida_volta == 'ida':
    print('Sua viagem vai custar R$ 500.')
elif destinoresp == 'Região Norte' and ida_volta == 'ida e volta':
    print('Sua viagem vai custar R$ 900.')
elif destinoresp == 'Região Nordeste' and ida_volta == 'ida':
    print('Sua viagem vai custar R$ 350.')
elif destinoresp == 'Região Nordeste' and ida_volta == 'ida e volta':
    print('Sua viagem vai custar R$ 650.')
elif destinoresp == 'Região Centro-Oeste' and ida_volta == 'ida':
    print('Sua viagem vai custar R$ 350.')
elif destinoresp == 'Região Centro-Oeste' and ida_volta == 'ida e volta':
    print('Sua viagem vai custar R$ 600.')
elif destinoresp == 'Região Sul' and ida_volta == 'ida':
    print('Sua viagem vai custar R$ 300.')
elif destinoresp == 'Região Sul' and ida_volta == 'ida e volta':
    print('Sua viagem vai custar R$ 550.')


    






