print('======== Exercício 14 (Conversor de temperatura) ========')

conversorDe = input('O que você deseja fazer?\n1 - Conversor de Celsius para Fahrenheit\n2 - Conversor de Fahrenheit para Celsius\nOpção: ')
print('==========================================================')
if(conversorDe == '1'):
    temperatura = float(input('Informe a temperatura em Celsius: '))
    print('A temperatura de {} ºC equivale a {} ºF'.format(temperatura, (temperatura * (9 / 5)) + 32))
else:
    temperatura = float(input('Informe a temperatura em Fahrenheit: '))
    print('A temperatura de {} ºF equivale a {} ºC'.format(temperatura, (temperatura - 32) * (5 / 9)))
