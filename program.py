from pd_aut import *
from design import *



if __name__ == "__main__":
    input1 = 'ababbaba'
    input2 = 'abababab'
    input3 = 'aaabbbc'
    test_states = ["q1","q2","q3","q4"]
    test_input_symbols = ['a','b']
    test_stack_symbols = ['a','b']
    test_transitions = {'q1':[[epsilon,epsilon,'z0','q2']],
                        'q2':[['a',epsilon,'a','q2'],['b',epsilon,'b','q2'],[epsilon,epsilon,epsilon,'q3']],
                        'q3':[['a','a',epsilon,'q3'],['b','b',epsilon,'q3'],[epsilon,'z0',epsilon,'q4']]}
    test_start = 'q1'
    test_stack_s = 'z0'
    test_final = 'q4'

    simulation = pd_automata(input3,
                            test_states,
                            test_input_symbols,
                            test_stack_symbols,
                            test_transitions,
                            test_start,
                            test_stack_s,
                            test_final,
                            [[test_start,0]])

    # simulation.start_automata()

    Dialog.show()
    sys.exit(app.exec_())
    '''
    q1:epsilon,epsilon,z0,q2
    q2:a,epsilon,a,q2:b,epsilon,b,q2:epsilon,epsilon,epsilon,q3
    q3:a,a,epsilon,q3:b,b,epsilon,q3:epsilon,z0,epsilon,q4
    '''