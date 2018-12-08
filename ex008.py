print('======== Exercício 09 (Tabuada) ========')

valor = int(input('Informe o valor que você deseja gerar a tabuada: '))

print('Tabuada de {}:'.format(valor))
for i in range(0, 11):
    print('{} * {} = {}'.format(valor, i, valor * i))