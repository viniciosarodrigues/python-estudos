print('======== Exercício 11 (Calcula  área de uma parede ========')

altura = float(input('Informe a altura da parede: '))
largura = float(input('Informe a largura da parede: '))

print('A parede possui {}m², será necessário {}l de tinta para pintar a mesma.'.format(altura * largura, (altura * largura)/2))
