opo = float(input('informe o cateto oposto: '))
adj = float(input('informe o cateto adjacente: '))

import math

#op2 = math.pow(opo,2)
#aj2 = math.pow(adj,2)

#hip = op2 + aj2
#res = math.sqrt(hip)

hip = math.hypot(opo,adj)

print(hip)