class AFN2:
    def __init__(self):
        self.start_state = 'q0'
        self.state = self.start_state
        self.start_char = None

    def transition(self, char):
        if self.state == 'q0':
            self.start_char = char
            if char == 'a':
                self.state = 'q1'
            elif char == 'b':
                self.state = 'q2'
        elif self.state == 'q1' and char == 'a':
            self.state = 'qf'
        elif self.state == 'q2' and char == 'b':
            self.state = 'qf'
        else:
            self.state = 'q0'

    def is_accepted(self, input_string):
        self.state = self.start_state
        self.start_char = None
        if not input_string:
            return False
        for char in input_string[:-1]:
            self.transition(char)
        return input_string[-1] == self.start_char

# Testes
afn2 = AFN2()
test_cases = ["aa", "ab", "baba", "bb", "abba"]
print({case: afn2.is_accepted(case) for case in test_cases})
