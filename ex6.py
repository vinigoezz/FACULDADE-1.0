#Implemente um programa para calcular as raízes de uma equação do 2º grau, sendo que
#os valores dos coeficientes A, B, e C devem ser fornecidos pelo usuário, e os valores das
#raízes devem ser calculadas pela fórmula de Bhaskara, como segue:
#� = !"±√"!!%&'
#(&
import math
a = float(input("Digite o valor de A: "))
b = float(input("Digite o valor de B: "))
c = float(input("Digite o valor de C: "))
delta = b**2 - 4*a*c
if delta > 0:
    # Calcula as duas raízes
    x1 = (-b + math.sqrt(delta)) / (2*a)
    x2 = (-b - math.sqrt(delta)) / (2*a)
    print(f"As raízes são: x1 = {x1} e x2 = {x2}")
elif delta == 0:
   
    x = -b / (2*a)
    print(f"A raiz é única: x = {x}")
else:
   
    print("A equação não possui raízes reais")