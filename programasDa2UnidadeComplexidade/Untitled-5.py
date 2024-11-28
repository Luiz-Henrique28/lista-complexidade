class AFD_a_maior_que_b:
    def __init__(self):
        self.state = 'q0'

    def transition(self, symbol):
        if self.state == 'q0':
            self.state = 'q1' if symbol == 'a' else 'q2'
        elif self.state == 'q1':
            self.state = 'q1' if symbol == 'a' else 'q0'
        elif self.state == 'q2':
            self.state = 'q2'

    def is_accepted(self):
        return self.state == 'q1'

# Testando o AFD
afd_a_maior_que_b = AFD_a_maior_que_b()
test_cases = ['a', 'ab', 'aab', 'ba', 'bbb']
for case in test_cases:
    afd_a_maior_que_b.state = 'q0'
    for symbol in case:
        afd_a_maior_que_b.transition(symbol)
    print(f'Entrada "{case}" aceita: {afd_a_maior_que_b.is_accepted()}')
