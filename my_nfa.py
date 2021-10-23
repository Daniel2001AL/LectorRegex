from functools import reduce

def mk_nfa(Q, Sigma, Delta, Q0, F):
    newNFA = {"Q":Q, "Sigma":Sigma, "Delta":Delta, "Q0":Q0, "F":F}
    return(newNFA)
  

def step_nfa(N, q, c):
    assert(
        c in (N["Sigma"] | {""})
    ), "c given to step_nfa not in Sigma."
    assert(
        q in  N["Q"]
    ), "q given to step_nfa not in Q."

    if (q,c) in N["Delta"].keys():
        return  N["Delta"][(q,c)]
    else:
        return  set({})  

def run_nfa(N, S, s, chatty=False):    
    S = Eclosure(N, S)
    if s=="":
        return S
    else:
        return run_nfa(N, ec_step_nfa(N, S, s[0], chatty), s[1:], chatty)

def ec_step_nfa(N, S, c, chatty=False):
    post_c_state_sets = list(map(lambda st: step_nfa(N, st, c), S))

    post_c_states = reduce(lambda x,y: set(x) | set(y), post_c_state_sets, set({}))                                                                         
    Eclosed_post_c_states = Eclosure(N, post_c_states)

    if chatty:
        print("States reached = ", Eclosed_post_c_states)
    return Eclosed_post_c_states

def Eclosure(N, S):
    return Echelp(N, S, set({}))

def Echelp(Nfa, Allsofar, Previous):
    if (Allsofar == Previous):
        return Allsofar
    else:
        post_eps_state_sets = list(map(lambda q: step_nfa(Nfa, q, ""), Allsofar))
                         
        post_eps_states = reduce(lambda x, y: set(x) | set(y), post_eps_state_sets,set({}))
        return Echelp(Nfa= Nfa, Allsofar = set(post_eps_states) | 
                    set(Allsofar),Previous = Allsofar)

def accepts_nfa(N, s, chatty=False):
    Q0 = N["Q0"]
    if (run_nfa(N, Q0, s, chatty) & N["F"]) != set({}):
        if chatty:
            print("NFA accepts '" + s + 
                  "' by reaching " + 
                  str(run_nfa(N, Q0, s, False)))
        return True
    else:
        if chatty:
            print("NFA rejects '" + s + "'")
        return False