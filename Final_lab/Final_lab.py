class MooreMachine:
    def __init__(self):
        self.states = {
            'A_A': 'A',
            'B_B': 'B', 
            'C_A': 'A',
            'D_C': 'C',
            'E_C': 'C',
            'C_C': 'C'
        }
        #transition table 
        self.transitions = {
            'A_A': {'0': 'A_A', '1': 'B_B'},
            'B_B': {'0': 'C_A', '1': 'D_C'},
            'C_A': {'0': 'D_C', '1': 'B_B'},
            'D_C': {'0': 'B_B', '1': 'C_C'},
            'E_C': {'0': 'D_C', '1': 'E_C'},
            'C_C': {'0': 'D_C', '1': 'B_B'}
        }
    
    def process_input(self, input_string, initial_state='A_A'):
        current_state = initial_state
        output_sequence = ""  
        output_sequence += self.states[current_state]
        
        for symbol in input_string:
            if symbol in ['0', '1']:
                current_state = self.transitions[current_state][symbol]
                output_sequence += self.states[current_state]
            else:
                raise ValueError(f"Invalid input symbol: {symbol}")            
        return output_sequence

def test_moore_machine():
    machine = MooreMachine()
    
    test_inputs = [
        "00110",
        "11001", 
        "1010110",
        "101111"
    ]
    
    print("Moore Machine Results:")
    print("Input\t\tOutput")
    print("----------------------")
    
    for input_str in test_inputs:
        try:
            output = machine.process_input(input_str)
            print(f"{input_str}\t\t{output}")
        except Exception as e:
            print(f"{input_str}\t\tError: {e}")

if __name__ == "__main__":
    test_moore_machine()