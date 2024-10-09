def afn_contem_101_ou_110(s):
    return '101' in s or '110' in s

# Testes
print(afn_contem_101_ou_110("1101"))  # True
print(afn_contem_101_ou_110("1001"))  # False
