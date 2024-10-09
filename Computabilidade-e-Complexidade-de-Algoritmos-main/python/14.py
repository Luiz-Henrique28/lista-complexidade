def afn_sem_11_ou_00(s):
    return '11' not in s and '00' not in s

# Testes
print(afn_sem_11_ou_00("1010"))  # True
print(afn_sem_11_ou_00("1100"))  # False
