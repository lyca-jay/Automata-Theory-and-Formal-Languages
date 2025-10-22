class MooreMachine:
    def __init__(self):
        # State and associated output (State: Output)
        self.state_output = {
            'A': '0',
            'B': '0',
            'C': '1'
        }
        
        # Transition function: {Current State: {Input: Next State}}
        self.transitions = {
            'A': {'1': 'B', '0': 'C'},
            'B': {'1': 'B', '0': 'C'},
            'C': {'0': 'C', '1': 'B'}
        }
        
        # Initial state
        self.current_state = 'A'

    def process_input(self, input_string):
        output_sequence = self.state_output[self.current_state]
        for symbol in input_string:
            if symbol not in ['0', '1']:
                print(f"Error: Invalid input symbol '{symbol}'. Stopping.")
                return ""
            
            #Get next state
            next_state = self.transitions[self.current_state][symbol]

            #Update current state
            self.current_state = next_state
            
            #Append output for *new* current state
            output_sequence += self.state_output[self.current_state]
            
        return output_sequence

#Example usage

machine = MooreMachine()
input_sequence = "1010" 

print(f"Input: {input_sequence}")
final_output = machine.process_input(input_sequence)
print(f"Output: {final_output}")
