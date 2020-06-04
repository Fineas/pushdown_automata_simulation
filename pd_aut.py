from pwn import *

epsilon = 'ε'

class stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def current_top(self):
        return self.items[self.size()-1]

    def size(self):
        return len(self.items)

class pd_automata:

    class simulation_state:
        def __init__(self, input_ch, current_state):
            self.input_ch = input_ch
            self.current_state = current_state

    def __init__(self, INPUT, s_states, s_input_alph, s_stack_alph, transitions, start, initial, s_acc_states, path):
        self.s_states = s_states
        self.s_input_alph = s_input_alph
        self.s_stack_alph = s_stack_alph
        self.transitions = transitions
        self.initial = initial
        self.s_acc_states = s_acc_states
        self.start = start

        self.path = path
        self.stack = stack()
        INPUT = [epsilon+i for i in INPUT]; self.INPUT = ''.join(INPUT) + epsilon
        self.state = 0

    def start_automata(self):
        print ('[*] Starting simulation')
        self.state = self.simulation_state(0,self.start)
        if self.next_step(self.stack):
            print ("[^] Word {} is accepted by the language.".format(self.INPUT))
        else:
            print ("[!] Word {} is not accepted by the language.".format(self.INPUT))
        self.end_simulation()

    def next_step(self, current_stack):
        if self.state != 0:
            # if we are in an ending state and there is no more input to get it means that the simulation ended
            print ('!!!',self.state.current_state,self.stack.size(),self.state.input_ch)
            if self.state.current_state in self.s_acc_states:
                if self.stack.size() == 0 and self.state.input_ch >= len(self.INPUT):
                    print ('[*] End of simulation')
                    self.end_simulation()
                    return 1
                else:
                    return 0
            if self.state.input_ch >= len(self.INPUT):
                return 0
            print ('[====================] Next Simulation Step [{}][{}] | {}'.format(self.state.current_state,self.INPUT[self.state.input_ch],current_stack.items))
            print ("[*] Available options: ",self.transitions[self.state.current_state])
            # iterez prin tranzitiile din state respectiv si caut daca pentru inputul curent pot merge undeva
            for i in (self.transitions[self.state.current_state]):
                print (">",i)
                # am gaist o tranzitie pentru inputul meu
                if i[0] == self.INPUT[self.state.input_ch]:
                    print ("[{}] Input accepted".format(self.INPUT[self.state.input_ch]))
                    # daca stack size != 0 inseamna ca se pot face pop-uri
                    if current_stack.size():
                        # se efectueaza pop in tranzitia asta
                        if i[1] != epsilon:
                            # efectual tranzitia decat daca top of stack == pop din tranzitie
                            if current_stack.current_top() == i[1]:
                                print ("[*] Current top matches!")
                                current_stack.pop()
                                print(" [*] Popped value {}".format(i[1]))
                                if i[2] != epsilon:
                                    current_stack.push(i[2])
                                    print (" [*] Pushed value {} to the stack".format(current_stack.current_top()))
                                    self.state.input_ch += 1
                                    self.state.current_state = i[3]
                                    print ("[*] New state {}".format(i[3]))
                                    self.path.append([self.state.current_state,self.state.input_ch])
                                    if self.next_step(current_stack):
                                        return 1
                                    else:
                                        self.path.pop()
                                        self.state.current_state = self.path[-1][0]
                                        self.state.input_ch = self.path[-1][1]
                                        if self.INPUT[self.state.input_ch] == epsilon:
                                            self.state.input_ch += 1
                                            self.path[-1][1] += 1
                                            if self.next_step(current_stack):
                                                return 1
                                            else:
                                                return 0
                                        print ("Fara succes6 | we are in state {} and input is {}".format(self.state.current_state,self.state.input_ch))
                                        continue
                                else:
                                    self.state.input_ch += 1
                                    self.state.current_state = i[3]                                
                                    print ("[*] New state {}".format(i[3]))
                                    self.path.append([self.state.current_state,self.state.input_ch])
                                    if self.next_step(current_stack):
                                        return 1
                                    else:
                                        self.path.pop()
                                        self.state.current_state = self.path[-1][0]
                                        self.state.input_ch = self.path[-1][1]
                                        if self.INPUT[self.state.input_ch] == epsilon:
                                            self.state.input_ch += 1
                                            self.path[-1][1] += 1
                                            if self.next_step(current_stack):
                                                return 1
                                            else:
                                                return 0
                                        print ("Fara succes5 | we are in state {} and input is {}".format(self.state.current_state,self.state.input_ch))
                                        continue
                            else:
                                if self.INPUT[self.state.input_ch] == epsilon:
                                    self.state.input_ch += 1
                                    self.path[-1][1] += 1
                                    if self.next_step(current_stack):
                                        return 1
                                    else:
                                        return 0
                                print ("[!] Current top is not matching")
                                return 0
                        # in tranzitia asta pop-ul e epsilon, deci nu se face
                        else:
                            print (' [*] No poping is done')
                            # verificam daca se fac push-uri in tranzitia asta
                            if i[2] != epsilon:
                                current_stack.push(i[2])
                                print (" [*] Pushed value {} to the stack".format(current_stack.current_top()))
                                self.state.input_ch += 1
                                self.state.current_state = i[3]
                                print ("[*] New state {}".format(i[3]))
                                self.path.append([self.state.current_state,self.state.input_ch])
                                if self.next_step(current_stack):
                                    return 1
                                else:
                                    print ("Acuma state trce arata asa:",self.path)
                                    self.path.pop()
                                    self.state.current_state = self.path[-1][0]
                                    self.state.input_ch = self.path[-1][1]
                                    if self.INPUT[self.state.input_ch] == epsilon:
                                        self.state.input_ch += 1
                                        self.path[-1][1] += 1
                                        if self.next_step(current_stack):
                                            return 1
                                        else:
                                            return 0
                                    print ("Fara succes4 | we are in state {} and input is {}".format(self.state.current_state,self.state.input_ch))
                                    continue
                            else:
                                self.state.input_ch += 1
                                self.state.current_state = i[3]                                
                                print ("[*] New state {}".format(i[3]))
                                self.path.append([self.state.current_state,self.state.input_ch])
                                if self.next_step(current_stack):
                                    return 1
                                else:
                                    print ("Acuma state trce arata asa:",self.path)
                                    self.path.pop()
                                    self.state.current_state = self.path[-1][0]
                                    self.state.input_ch = self.path[-1][1]
                                    if self.INPUT[self.state.input_ch] == epsilon:
                                        self.state.input_ch += 1
                                        self.path[-1][1] += 1
                                        if self.next_step(current_stack):
                                            return 1
                                        else:
                                            return 0
                                    print ("Fara succes3 | we are in state {} and input is {}".format(self.state.current_state,self.state.input_ch))
                                    continue
                    # daca stack size != 0 nu se pot face pop-uri
                    else:
                        print ('[!] Stack is empty')
                        if i[1] != epsilon:
                            print ('[!] Error, cannot pop because stack is empty')
                            return 0
                        # desi stack e empty, nu se fac pop-uri
                        else:
                            # verificam daca push-uri se fac
                            if i[2] != epsilon:
                                current_stack.push(i[2])
                                print (" [*] Pushed value {} to the stack".format(current_stack.current_top()))
                                print (' [*] No poping is done')
                                self.state.input_ch += 1
                                self.state.current_state = i[3]
                                print ("[*] New state {}".format(i[3]))
                                self.path.append([self.state.current_state,self.state.input_ch])
                                if self.next_step(current_stack):
                                    return 1
                                else:
                                    self.path.pop()
                                    self.state.current_state = self.path[-1][0]
                                    self.state.input_ch = self.path[-1][1]
                                    if self.INPUT[self.state.input_ch] == epsilon:
                                        self.state.input_ch += 1
                                        self.path[-1][1] += 1
                                        if self.next_step(current_stack):
                                            return 1
                                        else:
                                            return 0
                                    print ("Fara succes2 | we are in state {} and input is {}".format(self.state.current_state,self.state.input_ch))
                                    continue
                            # nu se fac nici pushuri
                            else:
                                self.state.input_ch += 1
                                self.state.current_state = i[3]                                
                                print ("[*] New state {}".format(i[3]))
                                self.path.append([self.state.current_state,self.state.input_ch])
                                if self.next_step(current_stack):
                                    return 1
                                else:
                                    self.path.pop()
                                    self.state.current_state = self.path[-1][0]
                                    self.state.input_ch = self.path[-1][1]
                                    if self.INPUT[self.state.input_ch] == epsilon:
                                        self.state.input_ch += 1
                                        self.path[-1][1] += 1
                                        if self.next_step(current_stack):
                                            return 1
                                        else:
                                            return 0
                                    print ("Fara succes1 | we are in state {} and input is {}".format(self.state.current_state,self.state.input_ch))
                                    continue
                else:
                    print ("[!] This transition is not possible because of different input")
            # daca ajung aici, inseamna ca nu a fost aleasa nicio tranzitie, deci simularea moare!!!

            return 0
        else:
            print("[!] Simulation not started")

    def end_simulation(self):
        print ('[*] Simulation Ended')
        pass