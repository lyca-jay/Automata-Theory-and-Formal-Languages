def prob1(string):
    state = 'a'
    for input in string:
        if state == 'a':
            if input == '0': state = 'a'
            elif input == '1': state = 'b'
        elif state == 'b':
            if input == '0': state = '1'
            elif input== '1': state = '0'
        elif state ==  '1':
            if input in ['0', '1']: state = '1'
    return state == '1'


print("Problem 1 Test : ")
for s in ["10", "010", "100110", "00", "011100", "011"]:
    print(f"{s}: {'ACCEPTED' if prob1(s) else 'REJECTED'}")  
