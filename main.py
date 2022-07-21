def is_empty_input(user_input):
    return len(user_input) == 0


def is_binary_data(user_input):
    for k in user_input:
        if k != '0' and k != '1':
            return False
    return True


def calculate_nrz(user_input):
    output = []
    for k in user_input:
        output.append(int(k))
    return output


def calculate_nrzl(user_input):
    output = []
    for k in user_input:
        if k == '1':
            output.append(1)
        else:
            output.append(-1)
    return output
