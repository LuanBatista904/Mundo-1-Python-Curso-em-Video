nome = str(input('Digite seu nome completo: '))
print(nome.upper())
print(nome.lower())
nomei = nome
nome = nome.replace(' ','')
print(len(nome))
nome = nomei
nome = nome.split()
print(len(nome[0]))