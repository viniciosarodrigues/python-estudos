print('============== Operadores numéricos ===============')

n1 = int(input('Informe um valor: '))
n2 = int(input('Informe um outro valor: '))

soma = n1 + n2
multi = n1 * n2
divis = n1 / n2
div = n1 // n2
elev = n1 ** n2
print('A soma é {}, o produto é {} e a divisão é {}'.format(soma, multi, divis))
print('A divisão inteira é {} e a potência de {} a {} é {}'.format(div, n1, n2, elev))
