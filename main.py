import ast
from dfa import DFA
from nfa import NFA
from tkinter import Button, Entry, Label, Tk
from tkinter import filedialog
from tkinter import font, messagebox


def read_automata(filename):
    Auto_model = {}
    with open(filename,mode='r',encoding='utf-8') as f:
        for line in f:
            k, v = line.strip().split('=')
            Auto_model[k.strip()] = v.strip()
    Auto_model['S']  = Auto_model['S'][1:-1].replace(',','')
    s = set(Auto_model['S'])

    Auto_model['Q'] = Auto_model['Q'].replace('{','')
    Auto_model['Q'] = Auto_model['Q'].replace('}','')
    state_list = list(Auto_model['Q'].split(','))
    q = set(state_list)


    d = Auto_model['D']
    d = d.replace(' ','')
    d = d.replace('{(','(')
    d = d.replace(')}',')') 
    d = d.replace("(","('")
    d = d.replace(",","','") 
    d = d.replace(")','",",") 
    check_nfa = ',{'
    if check_nfa in Auto_model['D']:
        type_automata = 'NFA' 
        d = d.replace(",'{",",{") 
        d = d.replace("{","{'") 
        d = d.replace("}","'}") 
        d = d.replace("},","}),")     
    else:
        type_automata = 'DFA'
        d = d.replace(",(","),(") 
        d = d.replace(")","')") 
    delta =list(ast.literal_eval(d))
    states = {}
    for state in delta:
        states[(state[0],state[1])] = state[2]

    Auto_model['F'] = Auto_model['F'].replace('{','')
    Auto_model['F'] = Auto_model['F'].replace('}','')
    final_state_list = list(Auto_model['F'].split(','))

    final = set(final_state_list)
    Auto_model = {
        'S': s,
        'Q': q,
        'D': states,
        'q0':Auto_model['q0'],
        'F': final
    }
    return Auto_model,type_automata

def run_automata(automata,automata_type,string):
    if automata_type == 'NFA':
        my_nfa = NFA()
        res = my_nfa.nfa_simulation(string,automata)
    elif automata_type == 'DFA':
        my_dfa = DFA()
        res = my_dfa.accepts_dfa(string,automata)
    if res:
        response = 'La cadena es válida'
    else:
        response = 'La cadena NO es válida'
    return response

def open_file_automata():
    global filename
    filename = filedialog.askopenfilename(initialdir='./',title='Seleccionar un archivo',filetypes=(('text files','*.txt'),('all files',"*.*")))
    btn_process_word['state'] = 'active'

def start_automata():
    new_Automata,auto_type = read_automata(filename)
    string = text_field.get()
    result = run_automata(new_Automata,auto_type,string)
    messagebox.showinfo(message=result,title='Resultado')

if __name__ == '__main__':
    root = Tk()
    root.title('Generic Automata')
    root.geometry("600x250")
    btn_upload_auto = Button(root,text='Seleccionar Autómata', width=19,height=1, command=open_file_automata)
    btn_upload_auto.place(x=200,y=0)
    btn_upload_auto['font'] = font.Font(size=13)

    text_field = Entry(root, width=20)
    text_field['font'] = font.Font(size=12)
    text_field.place(x=200,y=100)

    btn_process_word = Button(root,text='Ejecutar Autómata', command=start_automata)
    btn_process_word['state'] = 'disabled'
    btn_process_word.place(x=220,y=200)
    btn_process_word['font'] = font.Font(size=13)
    root.mainloop()
    
