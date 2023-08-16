# Translation GUI
# 2022-6-24
# Eddy Liu-Lin

# Imports
import tkinter as tk
import re

# Create the GUI
gui = tk.Tk()
gui.geometry('450x200')
gui.title('mRNA Translator v1.3')
gui.resizable(False, False)

# Create window elements
input_label = tk.Label(text='请输入mRNA序列:')
input_text = tk.Entry(width=40)
output_label = tk.Label(text='转译结果:')
output_text = tk.Entry(width=40)
author = tk.Label(text='Made with Python by Eddy Liu-Lin')
date = tk.Label(text='Release Date: 2022-6-24')

# Display window elements
input_label.pack()
input_text.pack()
output_label.pack()
output_text.pack()
author.place(relx=0.51, rely=0.8)
date.place(relx=0.627, rely=0.9)

# Variables
mrna = ''
num = 0
num_in_string = 3
result = ''
end = ''
invalid_length = ''
error_in_end = ''
letter_check = ''
result_in_alpha = ''

#Definitions
def quit_program():
    gui.destroy()

def convert():
    mrna = input_text.get()
    result = ''
    num_in_string = 3
    num = int(len(mrna) / 3)
    invalid_length = ''
    error_in_end = ''

    # Translation rules
    def do(target):
        output = (target[num_in_string - 3:num_in_string])
        # Sequence for Start
        if output in ('AUG'):
            end = 'Start'
        # Sequence for Phe
        elif output in ('UUU', 'UUC'):
            end = 'Phe'
        # Sequence for Leu
        elif output in ('UUA', 'UUG', 'CUU', 'CUC', 'CUA', 'CUG'):
            end = 'Leu'
        # Sequence for Ser
        elif output in ('UCU', 'UCC', 'UCA', 'UCG', 'AGU', 'AGC'):
            end = 'Ser'
        # Sequence for Tyr
        elif output in ('UAU', 'UAC'):
            end = 'Tyr'
        # Sequence for Cys
        elif output in ('UGU', 'UGC'):
            end = 'Cys'
        # Sequence for Trp
        elif output in ('UGG'):
            end = 'Trp'
        # Sequence for Pro
        elif output in ('CCU', 'CCC', 'CCA', 'CCG'):
            end = 'Pro'
        # Sequence for His
        elif output in ('CAU', 'CAC'):
            end = 'His'
        # Sequence for Gln
        elif output in ('CAA', 'CAG'):
            end = 'Gln'
        # Sequence for Arg
        elif output in ('CGU', 'CGC', 'CGA', 'CGG', 'AGA', 'AGG'):
            end = 'Arg'
        # Sequence for Ile
        elif output in ('AUU', 'AUC', 'AUA'):
            end = 'Ile'
        # Sequence for Thr
        elif output in ('ACU', 'ACC', 'ACA', 'ACG'):
            end = 'Thr'
        # Sequence for Asn
        elif output in ('AAU', 'AAC'):
            end = 'Asn'
        # Sequence for Lys
        elif output in ('AAA', 'AAG'):
            end = 'Lys'
        # Sequence for Val
        elif output in ('GUU', 'GUC', 'GUA', 'GUG'):
            end = 'Val'
        # Sequence for Ala
        elif output in ('GCU', 'GCC', 'GCA', 'GCG'):
            end = 'Ala'
        # Sequence for Asp
        elif output in ('GAU', 'GAC'):
            end = 'Asp'
        # Sequence for Glu
        elif output in ('GAA', 'GAG'):
            end = 'Glu'
        # Sequence for Gly
        elif output in ('GGU', 'GGC', 'GGA', 'GGG'):
            end = 'Gly'
        # Sequence for Stop
        elif output in ('UAA', 'UAG', 'UGA'):
            end = 'Stop'
        else:
            end = ''
        return end
        

    #Start the loop
    for x in range(num):
        result = result + do(mrna.upper()) + ' '
        num_in_string = num_in_string + 3

    # Check if length of input is a multiple of 3
    if len(mrna) % 3 == 0:
        invalid_length = ''
    else:
        invalid_length = 'Error'

    #Check the input letters
    result_in_alpha = mrna.isalpha()

    # Check if input contains only valid characters
    letter_check = str(re.search('[BDEFHIJKLMNOPQRSTVWXYZ]', mrna.upper()))

    #Output判断开始
    #Invalid length
    if invalid_length == 'Error':
        #If mRNA not in alphabet
        if result_in_alpha == False:
            result = 'Invalid input: mRNA input contains numbers or symbols!'
        #If in alphabet but containing invalid letters
        elif letter_check != 'None':
            result = 'Invalid input: mRNA input contains invalid letter(s)!'
        #If in alphabet and does not containing invalid letters
        else:
            result = 'Invalid input: Invalid length!'
        #Print the error message
        output_text.delete(0, tk.END)
        output_text.insert(0, str(result))
    #Passed all error checks, display result
    elif invalid_length == '':
        if result_in_alpha == False:
            result = 'Invalid input: mRNA input contains numbers or symbols!'
        elif letter_check != 'None':
            result = 'Invalid input: mRNA input contains invalid letter(s)!'
        output_text.delete(0, tk.END)
        output_text.insert(0, str(result))


#Making Buttons
RunButton = tk.Button(text = '转译', height=2, width=6, command=convert)
quit_button = tk.Button(text = 'Quit', height=2, width=6, command=quit_program)
#Display Buttons
RunButton.place(relx=0.25, rely=0.6)
quit_button.place(relx=0.6, rely=0.6)


#Start
gui.mainloop()