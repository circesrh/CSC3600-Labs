from logic import *

#kanren stuff (basic math logic)
S = Symbol("Storm") #There is a storm today
D = Symbol("Darkseid") #Superman fought Darkseid
L = Symbol("Lex") #Superman fought Lex Luthor today

#kb = knowledge base
kb = And(
    Implication(Not(S), D), #Rule 1
    Or(D, L),
    Not(And(D, L)),#Rule 2
    L #Rule 3
)

#Question 1(d)
sentence = Implication(S, D)
print("Question 1(d)",sentence.formula())

#model checking
print(kb.formula())
print("Is there a storm? Answer:",model_check(kb, S))
print("Is Superman fighting Darkseid today? Answer:", model_check(kb, D))
print("Is he not fighting Lex Luthor? Answer:", model_check(kb, Not(L)))
print("Is it storming or is he fighting Darkseid? Answer:", model_check(kb, Or(S, D)))