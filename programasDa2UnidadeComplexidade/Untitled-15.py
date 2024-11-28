class MT5:
    def __init__(self):
        self.state = 'q0'

    def transition(self, char):
        if self.state == 'q0' and char == 'a':
            self.state = 'q1'
        elif self.state == 'q1' and char == 'a':
            self.state = 'q2'
        elif self.state == 'q2' and char == 'b':
            self.state = 'q_accept'
        else:
            self.state = 'q_reject'

    def is_accepted(self):
        return self.state == 'q_accept'

    def test_mt5(self, input_string):
        self.state = 'q0'
        for char in input_string:
            self.transition(char)
            if self.state == 'q_reject':
                return False
        return self.is_accepted()

# Testes
mt = MT5()
test_cases = ["aab", "aa", "ab", "baba", ""]
results = {case: mt.test_mt5(case) for case in test_cases}
print(results)
