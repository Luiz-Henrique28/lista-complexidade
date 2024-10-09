def afn_01_termina_10(s):
    return s.startswith('01') and s.endswith('10')

# Testes
print(afn_01_termina_10("0110"))  # True
print(afn_01_termina_10("0100"))  # False
