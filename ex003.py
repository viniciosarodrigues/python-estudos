print('======================= Exercício 1 (Trabalhando com Tipos de dados) ==========================')
valor = input('Digite algo: ')

print('O tipo primitivo desse valor é {}'.format(type(valor)))

if(valor.isspace()):
    print('\nEste valor só em espaços')

if(valor.isnumeric()):
    print('\nEste valor é numérico')

if(valor.isalpha()):
    print('\nEste valor é alfabético')

if (valor.isalnum()):
    print('\nEste valor é alfa-numérico')

if(valor.isupper()):
    print('\nEste valor está em maiúsculas')

if(valor.islower()):
    print('\nEste valor em minúsculas')
