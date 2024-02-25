class FiniteStateAutomaton:
    def __init__(self):
        self.states = {'START', 'ON', 'OFF'}
        self.alphabet = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '+', '-', '='}
        self.transitions = {'START': {'0': 'ON', '1': 'ON', '2': 'ON', '3': 'ON', '4': 'ON', '5': 'ON', '6': 'ON', '7': 'ON', '8': 'ON', '9': 'ON'},
                            'ON': {'0': 'ON', '1': 'ON', '2': 'ON', '3': 'ON', '4': 'ON', '5': 'ON', '6': 'ON', '7': 'ON', '8': 'ON', '9': 'ON', '+': 'OFF', '-': 'OFF', '=': 'PRINT'},
                            'OFF': {'0': 'OFF', '1': 'OFF', '2': 'OFF', '3': 'OFF', '4': 'OFF', '5': 'OFF', '6': 'OFF', '7': 'OFF', '8': 'OFF', '9': 'OFF', '+': 'OFF', '-': 'OFF'}}
        self.current_state = 'START'
        self.sum_result = 0
        self.temp_number = ""

    def reset(self):
        self.current_state = 'START'
        self.sum_result = 0
        self.temp_number = ""

    def process_input(self, input_text):
        i = 0
        while i < len(input_text):
            three_chars = input_text[i:i+3]

            if 'on' in three_chars:
                i += 1  # Skip two characters after 'on' (one after the loop incrementation and another here)
                self.current_state = 'ON'
            elif 'off' in three_chars:
                self.current_state = 'OFF'
                i += 2  # Skip three characters after 'off' (same here)
            elif '=' in three_chars:
                print("Current sum:", self.sum_result)
            elif input_text[i] in self.alphabet:
                if self.current_state == 'ON':
                    numbers = ''.join(c for c in three_chars if c.isdigit())
                    self.sum_result += int(numbers)     
            i += 1       
            
        return self.sum_result


# Create the Finite State Automaton
fsa = FiniteStateAutomaton()

# Process input sequences
input_sequence1 = 'on+123=off456='
result1 = fsa.process_input(input_sequence1)
print(f"Result for '{input_sequence1}': {result1}")

fsa.reset()
three_chars = ""
input_sequence2 = '456on+789ole345=off123='
result2 = fsa.process_input(input_sequence2)
print(f"Result for '{input_sequence2}': {result2}")
