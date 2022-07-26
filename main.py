from tkinter import *
import matplotlib.pyplot as plt
import numpy


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
        output.append(int(k))
    return output


def calculate_nrzl(user_input):
    output = []
    for k in user_input:
        if k == '1':
            output.append(1)
            output.append(1)
        else:
            output.append(-1)
            output.append(-1)
    return output


def calculate_nrzi(user_input):
    output = [1]
    index = 0
    for k in user_input:
        if k == '0':
            output.append(output[index])
            output.append(output[index])
            index += 2
        else:
            output.append(-output[index])
            output.append(-output[index])
            index += 2
    output.pop(0)
    return output


def calculate_bipolar_ami(user_input):
    output = []
    found_first_one = False
    number_of_ones = 0
    for k in user_input:
        if k == '0':
            output.append(0)
            output.append(0)
        else:
            if not found_first_one:
                output.append(1)
                output.append(1)
                found_first_one = True
                number_of_ones += 1
            else:
                dummy = (-1) ** number_of_ones
                output.append(dummy)
                output.append(dummy)
                number_of_ones += 1
    return output


def calculate_pseudoternary(user_input):
    output = []
    found_first_zero = False
    number_of_zeros = 0
    for k in user_input:
        if k == '1':
            output.append(0)
            output.append(0)
        else:
            if not found_first_zero:
                output.append(1)
                output.append(1)
                found_first_zero = True
                number_of_zeros += 1
            else:
                dummy = (-1) ** number_of_zeros
                output.append(dummy)
                output.append(dummy)
                number_of_zeros += 1
    return output


def calculate_manchester_encoding(user_input):
    output = []
    for k in user_input:
        if k == '1':
            output.append(0)
            output.append(0)
            output.append(1)
            output.append(1)
        else:
            output.append(1)
            output.append(1)
            output.append(0)
            output.append(0)
    return output


def calculate_differential_manchester(user_input):
    output = [0]
    index = 0
    for k in user_input:
        if k == '1':
            output.append(output[index])
            output.append(output[index])
            index += 2
            if output[index] == 0:
                output.append(1)
                output.append(1)
            else:
                output.append(0)
                output.append(0)
            index += 2
        else:
            if output[index] == 0:
                output.append(0)
                output.append(1)
                output.append(1)
                output.append(0)
                output.append(0)
            else:
                output.append(1)
                output.append(0)
                output.append(0)
                output.append(1)
                output.append(1)
            index += 5
    output.pop(0)
    return output


def visualise_nrz(output, input):
    x_axis = [0, 1]
    index = 1
    for k in range(1, len(input)):
        if input[k - 1] != input[k]:
            x_axis.append(x_axis[len(x_axis) - 1])
            index += 1
            x_axis.append(index)
        else:
            x_axis.append(index)
            index += 1
            x_axis.append(index)
    plt.plot(x_axis, output)
    plt.ylim(-1, 2)
    plt.xlim(0, index)
    plt.show()


def visualise_nrzl(output, input):
    x_axis = [0, 1]
    index = 1
    for k in range(1, len(input)):
        if input[k - 1] != input[k]:
            x_axis.append(x_axis[len(x_axis) - 1])
            index += 1
            x_axis.append(index)
        else:
            x_axis.append(index)
            index += 1
            x_axis.append(index)
    plt.plot(x_axis, output)
    plt.ylim(-2, 2)
    plt.xlim(0, index)
    plt.show()


def visualise_nrzi(output, input):
    x_axis = [0, 1]
    index = 1
    for k in range(1, len(input)):
        if input[k] == '1':
            x_axis.append(x_axis[len(x_axis) - 1])
            index += 1
            x_axis.append(index)
        else:
            x_axis.append(index)
            index += 1
            x_axis.append(index)
    plt.plot(x_axis, output)
    plt.ylim(-2, 2)
    plt.xlim(0, index)
    plt.show()


def visualise_bipolar_ami(output, input):
    x_axis = [0, 1]
    index = 1
    for k in range(1, len(input)):
        if input[k] == '0' and input[k - 1] == '0':
            index += 1
            x_axis.append(index)
            index += 1
            x_axis.append(index)
        else:
            x_axis.append(index)
            index += 1
            x_axis.append(index)
    plt.plot(x_axis, output)
    plt.ylim(-2, 2)
    plt.xlim(0, index)
    plt.show()


def visualise_pseudoternary(output, input):
    x_axis = [0, 1]
    index = 1
    for k in range(1, len(input)):
        if input[k] == '1' and input[k - 1] == '1':
            index += 1
            x_axis.append(index)
            index += 1
            x_axis.append(index)
        else:
            x_axis.append(index)
            index += 1
            x_axis.append(index)
    plt.plot(x_axis, output)
    plt.ylim(-2, 2)
    plt.xlim(0, index)
    plt.show()


def visualise_manchester_encoding(output, input):
    x_axis = [0, 1, 1, 2]
    index = 2
    for k in range(1, len(input)):
        x_axis.append(index)
        index += 1
        x_axis.append(index)
        x_axis.append(index)
        index += 1
        x_axis.append(index)
    plt.plot(x_axis, output)
    plt.ylim(-0.5, 1.5)
    plt.xticks(numpy.arange(0, 2 * len(input) + 0.05, step=1), rotation=90)
    plt.show()


def visualise_differential_manchester(output, input):
    x_axis = []
    index = 0
    for k in input:
        if k == '1':
            x_axis.append(index)
            index += 1
            x_axis.append(index)
            x_axis.append(index)
            index += 1
            x_axis.append(index)
        else:
            x_axis.append(index)
            x_axis.append(index)
            index += 1
            x_axis.append(index)
            x_axis.append(index)
            index += 1
            x_axis.append(index)
    plt.plot(x_axis, output, linewidth=3)
    plt.ylim(-0.5, 1.5)
    plt.xticks(numpy.arange(0, 2 * len(input) + 0.05, step=1), rotation=90)
    plt.show()


def graph_input():
    inp = binary_sequence.get(1.0, "end-1c")
    print(inp)


root = Tk()
root['background'] = 'white'
root.title("Binary Encoding Visualisation")

window_width = int(root.winfo_reqwidth()) * 3.5
window_height = int(root.winfo_reqheight()) * 3.5

positionRight = int(root.winfo_screenwidth() / 2 - window_width / 2)
positionDown = int(root.winfo_screenheight() / 2 - window_height / 2)

root.geometry(
    "{}{}+{}+{}".format(str(int(window_width)) + 'x', str(int(window_height)), str(positionRight), str(positionDown)))

label = Label(root, text="Insert binary data")
label.pack()

button = Button(root, text="Graph", command=graph_input)
button.pack()

binary_sequence = Text(root,height=int(window_height/200),width=int(window_width//8))
binary_sequence.pack()

root.mainloop()
