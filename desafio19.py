n1 = str(input('Informe o primeiro aluno: '))
n2 = str(input('Informe o segundo aluno: '))
n3 = str(input('informe oterceiro aluno: '))
n4 =  str(input('Informe o quarto aluno: '))
lista = [n1,n2,n3,n4]
from random import choices
escolhido = choices(lista)
print('o aluno escolhido foi {}!'.format(escolhido))