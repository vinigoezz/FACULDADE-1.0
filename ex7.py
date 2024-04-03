dia = int(input("Digite o dia de nascimento (1-31): "))
mes = int(input("Digite o mês de nascimento (1-12): "))
ano = int(input("Digite o ano de nascimento (4 dígitos): "))
formato = int(input("Escolha o formato de exibição (1-3): "))

meses = {
    1: "janeiro", 2: "fevereiro", 3: "março", 4: "abril",
    5: "maio", 6: "junho", 7: "julho", 8: "agosto",
    9: "setembro", 10: "outubro", 11: "novembro", 12: "dezembro"
}

if formato == 1:
    print(f"{dia:02d}/{mes:02d}/{ano}")
elif formato == 2:
    print(f"{dia:02d}/{meses[mes][:3]}/{ano}")
elif formato == 3:
    print(f"{dia} de {meses[mes]} de {ano}")
else:
    print("Formato inválido")
