def afd_inicio_fim_igual(s):
    if len(s) < 1:
        return False
    return s[0] == s[-1]

# Testes
print(afd_inicio_fim_igual("101"))  # True
print(afd_inicio_fim_igual("100"))  # False
