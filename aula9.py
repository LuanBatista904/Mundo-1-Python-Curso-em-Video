from itertools import count


frase = str('Curso em Video Python')
print(frase[9::3])
print(frase.count('o'))
print(len(frase))
print(frase.replace('Python','Android'))
print(frase.upper())
print(frase.lower())
print(frase.title())
print(frase.capitalize())
frase = '   Aprenda Python  '
print(frase.rstrip())
print(frase.lstrip())
print(frase.strip())
frase = frase.split()
print(frase)
' '.join(frase)

print("""wekjegfdfhkgbkgfhsggfgkbhfgbbfg
afgjlbnfg;nfgbfgm,nfng
gfnalnfsagnbfgfgn""")

print('curso' in frase)
