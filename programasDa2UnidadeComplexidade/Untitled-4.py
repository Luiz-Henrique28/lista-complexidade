class AFD_sem_aa:
    def __init__(self):
        self.state = 'q0'

    def transition(self, symbol):
        if self.state == 'q0':
            self.state = 'q1' if symbol == 'a' else 'q0'
        elif self.state == 'q1':
            self.state = 'q2' if symbol == 'a' else 'q0'
        elif self.state == 'q2':
            self.state = 'q2'

    def is_accepted(self):
        return self.state in ['q0', 'q1']

# Testando o AFD
afd_sem_aa = AFD_sem_aa()
test_cases = ['ab', 'aab', 'ba', 'aa', 'bba']
for case in test_cases:
    afd_sem_aa.state = 'q0'
    for symbol in case:
        afd_sem_aa.transition(symbol)
    print(f'Entrada "{case}" aceita: {afd_sem_aa.is_accepted()}')
