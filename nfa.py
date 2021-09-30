from tkinter import messagebox

class NFA:
    def __init__(self) -> None:
        pass

    def nfa_recursive_sim(self,string, current, edges, accepting,sigma):
        if string == "":
            return current in accepting
        else:
            letter = string[0]
            if letter not in sigma:
                messagebox.showerror(title='No encontrado',message=f'El símbolo {letter} no está en el alfabeto')
                return False
            key = (current, letter)
            epsilon = False
            if key not in edges:
                key = (current, 'epsilon')
                epsilon = True
            if key in edges:
                if epsilon:
                    rest = string
                else:
                    rest = string[1:]
                states = edges[key]
                for state in states:
                    if self.nfa_recursive_sim(rest, state, edges, accepting,sigma):
                        return True
            return False

    def nfa_simulation(self,string, NFA):
        if string == "":
            return NFA['q0'] in NFA['F']
        else:
            letter = string[0]
            if letter not in NFA['S']:
                messagebox.showerror(title='No encontrado',message=f'El símbolo {letter} no está en el alfabeto')
                return False
            key = (NFA['q0'], letter)
            epsilon = False
            if key not in NFA['D']:
                key = (NFA['q0'], 'epsilon')
                epsilon = True
            if key in NFA['D']:
                if epsilon:
                    rest = string[0:]
                else:
                    rest = string[1:]
                states = NFA['D'][key]
                for state in states:
                    if self.nfa_recursive_sim(rest, state, NFA['D'], NFA['F'],NFA['S']):
                        return True
            return False