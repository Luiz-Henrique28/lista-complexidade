def afn_a_depois_b(s):
    for i in range(len(s) - 1):
        if s[i] == 'b' and s[i+1] != 'a':
            return False
    return True

# Testes
print(afn_a_depois_b("baa"))   # False
print(afn_a_depois_b("abab"))  # True
