class MealyMachine:
    def __init__(self):
        self.current_state = 'A'

    def get_transition(self, current_state, input_symbol):
        if current_state == 'A':
            if input_symbol == '0':
                return ('B', 'b')
            elif input_symbol == '1':
                return ('A', 'b')
        
        elif current_state == 'B':
            if input_symbol == '1':
                return ('A', 'a')
            elif input_symbol == '0':
                return ('C', 'b')
        
        elif current_state == 'C':
            if input_symbol == '0':
                return ('B', 'b')
            elif input_symbol == '1':
                return ('A', 'b')
        
        # Handle invalid input
        return (None, "Error")

    def process_input(self, input_string):
        output_sequence = ""
        print(f"Starting State: {self.current_state}")
        
        for symbol in input_string:
            next_state, current_output = self.get_transition(self.current_state, symbol)
            if next_state is None:
                print(f"Input Error: Invalid symbol '{symbol}'")
                break
            print(f" ({self.current_state}, Input {symbol}) -> (Next State: {next_state}, Output: {current_output})")

            # Update state and output
            self.current_state = next_state
            output_sequence += current_output
            
        return output_sequence

#Example usage:

machine = MealyMachine()
input_str = "01010"
print(f"\n--- Processing Input: {input_str} ---")
final_output = machine.process_input(input_str)

print(f"\nInput Sequence: {input_str}")
print(f"Output Sequence: {final_output}")