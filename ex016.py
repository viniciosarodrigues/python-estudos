import math
print('======== Exercício 16 (Calculando hipotenusa) ========')

catetoUm = float(input("Informe o tamanho do primeiro cateto: "))
catetoDois = float(input("Informe o tamanho do segundo cateto: "))

print("Cateto um tem {}cm, o cateto dois tem {}cm e a hipotenusa mede aproximadamente {}cm".format(catetoUm, catetoDois, (math.hypot(catetoUm, catetoDois))))
