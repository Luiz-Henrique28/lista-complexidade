def afn_a_antes_de_b(s):
    return 'ba' not in s

# Testes
print(afn_a_antes_de_b("aaabbb"))  # True
print(afn_a_antes_de_b("abba"))    # False
