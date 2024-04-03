# Solicita a data com hora
dia = int(input("Digite o dia (1-31): "))
mes = int(input("Digite o mês (1-12): "))
ano = int(input("Digite o ano (4 dígitos): "))
hora = int(input("Digite a hora (0-23): "))
minuto = int(input("Digite o minuto (0-59): "))
segundo = int(input("Digite o segundo (0-59): "))

# Verifica se o ano é bissexto
bissexto = (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0)

# Pergunta ao usuário que informação deseja acrescentar e em qual quantidade
opcao = int(input("Que informação você deseja acrescentar? (1 - segundo, 2 - minuto, 3 - hora, 4 - dia, 5 - mês, 6 - ano): "))
quantidade = int(input("Quantidade a ser acrescentada: "))

# Atualiza a data com base na escolha do usuário
if opcao == 1:
    segundo += quantidade
    if segundo >= 60:
        segundo -= 60
        minuto += 1
elif opcao == 2:
    minuto += quantidade
    if minuto >= 60:
        minuto -= 60
        hora += 1
elif opcao == 3:
    hora += quantidade
    if hora >= 24:
        hora -= 24
        dia += 1
elif opcao == 4:
    dia += quantidade
    if mes in [1, 3, 5, 7, 8, 10, 12]:
        if dia > 31:
            dia -= 31
            mes += 1
    elif mes in [4, 6, 9, 11]:
        if dia > 30:
            dia -= 30
            mes += 1
    elif mes == 2:
        if bissexto and dia > 29:
            dia -= 29
            mes += 1
        elif not bissexto and dia > 28:
            dia -= 28
            mes += 1
elif opcao == 5:
    mes += quantidade
    if mes > 12:
        mes -= 12
        ano += 1
elif opcao == 6:
    ano += quantidade

# Verifica se o ano é bissexto após as modificações
bissexto_novo = (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0)

# Verifica se o dia 29 de fevereiro precisa ser ajustado
if not bissexto_novo and mes == 2 and dia == 29:
    dia = 28

# Exibe a nova data
print(f"Nova data: {dia:02d}/{mes:02d}/{ano} {hora:02d}:{minuto:02d}:{segundo:02d}")

