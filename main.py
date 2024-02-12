from automata.fa.dfa import *
import re

def verificarBinario(cadena):
    if not re.match(r'^[01/]*$', cadena):
        return False
    return True

def crearAutomata1():
    automata = DFA(
        states = {'q0', 'q1', 'q2'},
        input_symbols={'0', '1', '/'},
        transitions={
            'q0': {'0': 'q0', '1': 'q1', '/': 'q0'},
            'q1': {'0': 'q2', '1': 'q0', '/': 'q1'},
            'q2': {'0': 'q1', '1': 'q2', '/': 'q2'}
        },
        initial_state='q0',
        final_states={'q0'}
    )
    return automata

def multiploTres(cadena):
    automata = crearAutomata1()
    estadoActual = automata.initial_state

    for char in cadena:
        estadoActual = automata.transitions[estadoActual][char]

    if estadoActual in automata.final_states:
        return True
    else:
        return False


if __name__ == "__main__":
    
    cadena = str(input("Ingrese cualquier cadena en binario (Ingresar cadena vacía = /): "))
    
    if verificarBinario(cadena):
        if multiploTres(cadena):
            print(f"The DFA accepts the string '{cadena}'")
        else:
            print(f"The DFA rejects the string '{cadena}'") 
    else:
        print(f"The DFA rejects the string '{cadena}'") 