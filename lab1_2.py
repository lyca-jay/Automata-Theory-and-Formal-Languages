def prob2 (string):
    state = 'q0' 
    for input in string :
        if state == 'q0':
            if input == 'a': state = 'q1'
            elif input == 'b': state = 'q2'
        elif state == 'q1':
            if input == 'a': state = 'q0'
            elif input == 'b': state = 'q3'
        elif state == 'q2':
            if input == 'a': state = 'q3'
            elif input == 'b': state = 'q0'
        elif state == 'q3':
            if input == 'a': state = 'q2'
            elif input == 'b': state = 'q1'
    return state == 'q3'

print("Problem 2 Test : ")
for s in ["baaa", "ab", "babb", "bab", "abaab", "baaba"]:
    print(f"{s}: {'ACCEPTED' if prob2(s) else 'REJECTED'} ")   