def afd_exatamente_um_ab(s):
    return s.count('ab') == 1

# Testes
print(afd_exatamente_um_ab("abab"))  # False
print(afd_exatamente_um_ab("aab"))   # True
