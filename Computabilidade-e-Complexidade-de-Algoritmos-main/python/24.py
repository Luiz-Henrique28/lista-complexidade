def afd_duas_vezes_010(s):
    return s.count('010') >= 2

# Testes
print(afd_duas_vezes_010("0101010"))  # True
print(afd_duas_vezes_010("101010"))   # False
