def afd_exatamente_dois_uns(s):
    estado = 'q0'
    for char in s:
        if estado == 'q0':
            if char == '1':
                estado = 'q1'
        elif estado == 'q1':
            if char == '1':
                estado = 'q2'
        elif estado == 'q2':
            if char == '1':
                estado = 'q3'
        if estado == 'q3':
            break  # Mais de dois '1's, rejeita
    return estado == 'q2'

# Testes
print(afd_exatamente_dois_uns("1100"))  # True
print(afd_exatamente_dois_uns("111"))   # False
