num = int(input('Digite um valor entre 1000 e 9999: '))
u =  num // 1 % 10
d = num // 10 % 10
c = num //100%10
m = num //100%10
print('Unidade: {}\nDezena: {}\nCentena: {}\nMilhar:{}'.format(u, d, c, d))