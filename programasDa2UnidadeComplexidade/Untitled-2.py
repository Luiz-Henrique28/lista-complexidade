class AFD_termina_com_ab:
    def __init__(self):
        self.state = 'q0'

    def transition(self, symbol):
        if self.state == 'q0':
            self.state = 'q1' if symbol == 'a' else 'q0'
        elif self.state == 'q1':
            self.state = 'q2' if symbol == 'b' else 'q1'
        elif self.state == 'q2':
            self.state = 'q1' if symbol == 'a' else 'q0'

    def is_accepted(self):
        return self.state == 'q2'

# Testando o AFD
afd_ab = AFD_termina_com_ab()
test_cases = ['ab', 'aab', 'ba', 'aba', 'ababa']
for case in test_cases:
    afd_ab.state = 'q0'
    for symbol in case:
        afd_ab.transition(symbol)
    print(f'Entrada "{case}" aceita: {afd_ab.is_accepted()}')
