def afn_termina_01(s):
    return s.endswith('01')

# Testes
print(afn_termina_01("1101"))  # True
print(afn_termina_01("1000"))  # False
